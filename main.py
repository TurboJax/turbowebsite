# TODO: Add image/video/document viewers to /files so you don't need to download everything.

from flask import Flask, flash, request, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup
from jinja2 import TemplateNotFound
import requests
import datetime
import os
import sys
import typing
import errno

def filesize_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.2f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "Not Found")

allowed_dirs = os.getenv("ALLOWED_DIRS", "").split(",")

if app.secret_key == "Not Found":
    sys.exit(1)

env = app.jinja_env

def http_error(code: int, **kwargs) -> tuple:
    """
    Gets the page for the http error code.
    All error code pages should be created as jinja templates.

    Parameters:
        code (int): The HTTP error code to get the page for.

    Returns:
        tuple: The html response and the error code
    """
    return render_template(f"errors/{code}.j2", **kwargs), code

def render_jinja(template: str, **kwargs) -> str | tuple:
    """
    Renders a jinja2 template.
    If the template is not found, it renders the 404 error.

    Parameters:
        template (str): The jinja template to render.

    Returns:
        str: The rendered template
        tuple: The 404 page and error code 404
    """
    try:
        # Rendering the template
        return env.get_template(template).render(**kwargs)
    except TemplateNotFound:
        # 404 because the template could not be found
        return http_error(404)

def render_html(html_path: str) -> str | tuple:
    """
    Renders an html file.

    Parameters:
        html_path (str): The path to the html file, starting from the templates directory.

    Returns:
        str: The html page
        tuple: The 404 page and error code 404
    """
    try:
        # Loading the html
        with open(f"templates/{html_path}", "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        # 404 because the file could not be found
        return http_error(404)

def render_md(md_path: str) -> str | tuple:
    """
    Renders a markdown file.
    If the markdown file is not found, it renders the 404 error.

    NOTE:
        To allow the pages to define their title and header, the first two lines of the md file should be the title and header values respectively.
        These lines are not rendered in the body of the page.

    Parameters:
        md_path (str): The path to the markdown file, starting from the templates directory.

    Returns:
        str: The rendered page
        tuple: The 404 page and error code 404
    """
    try:
        # Getting the markdown template
        template = env.get_template("util/raw_md.j2")

        # Reading the markdown file
        with open(f"templates/{md_path}", "r") as file:
            title = file.readline()
            header = file.readline()
            data = file.read()

        # Rendering the template
        return template.render(md=data, title=title, header=header)
    except FileNotFoundError:
        # 404 because the markdown file could not be found
        return http_error(404)
    except TemplateNotFound:
        # 404 because the template could not be found.  This is a major issue
        print("Could not find the core \"util/raw_md.j2\" template!")
        return http_error(404)

@app.get("/<path:query>")
def query(query):
    # Checking if the query points to a file the server is equipped to handle
    if os.path.isfile(f"templates/{query}.md"):
        return render_md(f"{query}.md")
    if os.path.isfile(f"templates/{query}.j2"):
        return render_jinja(f"{query}.j2")
    if os.path.isfile(f"templates/{query}.html"):
        return render_html(f"{query}.html")

    # Checking if the query is a directory.  If it is, it will search for an index file
    if os.path.isdir(f"templates/{query}"):
        if os.path.isfile(f"templates/{query}/index.md"):
            return render_md(f"{query}/index.md")
        if os.path.isfile(f"templates/{query}/index.j2"):
            return render_jinja(f"{query}/index.j2")
        if os.path.isfile(f"templates/{query}/index.html"):
            return render_html(f"{query}/index.html")

    # No good file found, return 404
    return http_error(404)

def safe_strip(value: str | None) -> str:
    if isinstance(value, str):
        return value.strip()

    return ""

def path_sort(prefix: str, items: list[str]) -> list[str]:
    dirs = []
    files = []
    for item in items:
        if os.path.isdir(prefix + item):
            dirs.append(item)
        else:
            files.append(item)

    dirs.sort()
    files.sort()
    return dirs + files

@app.route("/")
def index():
    return render_jinja('index.j2')

@app.route("/javadocs/<project>")
@app.route("/javadocs/<project>/")
def redirect_to_javadocs(project):
    return redirect(f"/javadocs/{project}/index.html", code=302)

@app.route("/javadocs/<project>/<path:path>")
def javadocs(project, path=""):
    if path == "":
        return send_from_directory(f"javadocs/{project}/", "index.html")
    return send_from_directory(f"javadocs/{project}", path)

@app.route("/resume.pdf")
def resume():
    return send_from_directory("static/files", "resume.pdf")

@app.route('/files')
@app.route('/files/')
@app.route('/files/<path:subpath>')
def list_directory(subpath=""):
    subpath = str(subpath)
    abs_path = os.path.join('/mnt/drive1/files', subpath)

    if not os.path.exists(abs_path):
        return render_template("errors/404.j2"), 400

    if os.path.isfile(abs_path):
        # If it's a file, serve it for download
        return send_from_directory(os.path.dirname(abs_path), os.path.basename(abs_path), as_attachment=True)

    if subpath.startswith("priv"):
        is_allowed = False
        for allowed_dir in allowed_dirs:
            if allowed_dir == "":
                continue
            if subpath.startswith(f"priv/{allowed_dir}"):
                is_allowed = True
                break
        if not is_allowed:
            return http_error(404)

    # Get a list of files and subdirectories
    longest_name = 0
    items = []
    labels = []
    for item in path_sort(abs_path, os.listdir(abs_path)):
        # Hiding the priv folder
        if subpath == "" and item == "priv":
            continue

        item_path = os.path.join(abs_path, item)

        try:
            os.stat(item_path)
        except OSError as e:
            if e.errno == errno.ENOENT:
                labels.append("stat failed")
                items.append({'name':item, 'size':"-", 'last_modified': datetime.datetime.fromtimestamp(os.path.getmtime(abs_path))})
                continue
            else:
                raise e

        is_directory = os.path.isdir(item_path)
        size = filesize_fmt(os.path.getsize(item_path))
        if os.path.isdir(item_path):
            item = f"{item}/"
            size = "-"

        modified_datetime = datetime.datetime.fromtimestamp(os.path.getmtime(abs_path))
        items.append({'name':item, 'size':size, 'last_modified':modified_datetime})

        labels.append(f'<a href="{item_path[11::]}">')
        if len(item) > longest_name:
            longest_name = len(item)

    # Formatting the labels
    for i in range(len(labels)):
        if labels[i] == "stat failed":
            labels[i] = f"{items[i]['name'].ljust(longest_name, ' ')}  {items[i]['last_modified']}  {items[i]['size'].rjust(9, ' ')}"
        else:
            labels[i] += f"{items[i]['name'].ljust(longest_name, ' ')}</a>  {items[i]['last_modified']}  {items[i]['size'].rjust(9, ' ')}"

    return render_template('directory_listing.j2', labels=labels, current_path=subpath)

@app.get("/cnuclasses")
def cnuclasses():
    # TODO: Add a form that allows people to specify the semester to get info from.
    # When finding `semesterlist` values in the future, use the year but use the year + 1 if it is the fall semester.  XX is 00 for fall semester, 10 for spring semester, 20 for may term, 31 for summer term 1, and 32 for summer term 2.

    session = requests.Session()

    # Getting session cookies
    session.get("https://navigator.cnu.edu/StudentScheduleofClasses/socquery.aspx")

    # Defining the data to send
    data = {
        "__VIEWSTATE": "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",
        "__EVENTVALIDATION": "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",
        "semesterlist": "202610",
        "DisciplinesListBox": "All Courses",
        "Button1": "Search",
    }

    # Making the request
    response = session.post("https://navigator.cnu.edu/StudentScheduleofClasses/", data=data)

    # Parsing the output
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        classes = soup.tbody.find_all("tr")
    except Exception:
        return http_error(503, message="The schedule of classes decided to die for some reason.  Please wait for them to fix the issue.")

    return render_template("cnuclasses.j2", classes=classes, safe_strip=safe_strip)

# Run app
if __name__ == "__main__":
    app.run(debug=True, port=444, host="0.0.0.0")
