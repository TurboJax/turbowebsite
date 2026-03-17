from flask import Flask, flash, request, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup
from jinja2 import TemplateNotFound
from dotenv import load_dotenv
import jinja2
import mimetypes
import requests
import datetime
import os
import sys
import typing
import errno

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "Not Found")

# Preventing file uploads larger than 50MB
#app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

allowed_dirs = os.getenv("ALLOWED_DIRS", "").split(",")

if app.secret_key == "Not Found":
    sys.exit(1)

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

def render_jinja(template_path: str, **kwargs) -> str | tuple:
    """
    Renders a jinja2 template.
    If the template is not found, it renders the 404 error.

    Parameters:
        template_path (str): The path to the jinja template to render.

    Returns:
        str: The rendered template
        tuple: The 404 page and error code 404
    """
    try:
        # Rendering the template
        loader = jinja2.FileSystemLoader(["./templates", "/"])
        env = jinja2.Environment(loader=loader)
        return env.get_template(template_path).render(**kwargs)
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
        with open(html_path, "r") as file:
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
        template = app.jinja_env.get_template("util/raw_md.j2")

        # Reading the markdown file
        with open(md_path, "r") as file:
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
        app.logger.info("Could not find the core \"util/raw_md.j2\" template!")
        return http_error(404)

def filesize_fmt(num: float) -> str:
    """ Formats a number of bytes into different unit sizes. """
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024:
            return f"{num:3.2f}{unit}B"
        num /= 1024

    return f"{num:.1f}YiB"

def safe_strip(value: str | None) -> str:
    """ Safely checks if a value is a string before stripping extra whitespace from it. """
    return value.strip() if isinstance(value, str) else ""

def path_sort(dir: str, paths: list[str]) -> list[str]:
    """
    Sorts a list of paths in alphabetical order, separating directories and files.
    If a path does not exist, it is not included in the results.

    Parameters:
        dir (str): The parent directory of each path.
        paths (list[str]): The list of paths to sort.

    Returns:
        list[str]: The sorted list of directories and files
    """
    dirs = []
    files = []
    for path in paths:
        abs_path = os.path.join(dir, path)
        if os.path.isdir(abs_path):
            dirs.append(path)
        elif os.path.isfile(abs_path):
            files.append(path)

    dirs.sort()
    files.sort()
    return dirs + files

# App Routes

# Main static page getter
@app.get("/")
@app.get("/<path:query>")
def query(query=""):
    # Checking if the query points to a file the server is equipped to handle
    if os.path.isfile(f"templates/{query}.md"):
        return render_md(f"templates/{query}.md")
    if os.path.isfile(f"templates/{query}.j2"):
        return render_jinja(f"{query}.j2")
    if os.path.isfile(f"templates/{query}.html"):
        return render_html(f"templates/{query}.html")

    # Checking if the query is a directory.  If it is, it will search for an index file
    if os.path.isdir(f"templates/{query}"):
        if os.path.isfile(f"templates/{query}/index.md"):
            return render_md(f"templates/{query}/index.md")
        if os.path.isfile(f"templates/{query}/index.j2"):
            return render_jinja(f"{query}/index.j2")
        if os.path.isfile(f"templates/{query}/index.html"):
            return render_html(f"templates/{query}/index.html")

    # No good file found, return 404
    return http_error(404)

# Renders javadocs for the users
@app.route("/javadocs/<project>")
@app.route("/javadocs/<project>/")
@app.route("/javadocs/<project>/<path:path>")
def javadocs(project, path=""):
    if path == "":
        return redirect(f"/javadocs/{project}/index.html")

    return send_from_directory(f"javadocs/{project}", path)

# Sends my resume
@app.route("/resume.pdf")
def resume():
    return send_from_directory("static/files", "resume.pdf")

# File server
@app.route('/files')
@app.route('/files/')
@app.route('/files/<path:subpath>')
def list_directory(subpath=""):
    subpath = str(subpath)
    abs_path = os.path.join('/mnt/drive1/files', subpath)

    if not os.path.exists(abs_path):
        return render_template("errors/404.j2"), 404

    # If it is a file, try to load it or download it
    if os.path.isfile(abs_path):
        # Render HTML
        if abs_path.endswith(".html"):
            return render_html(abs_path)

        # Render MD
        if abs_path.endswith(".md"):
            return render_md(abs_path)

        # Render j2 (retains context from this app)
        if abs_path.endswith(".j2"):
            return render_jinja(abs_path)

        # Getting the mimetype
        mimetype, encoding = mimetypes.guess_type(abs_path)
        if mimetype is None:
            mimetype = "none"

        filetype = mimetype.split("/")[0]

        # Render image, audio, or video
        if filetype == "image" or filetype == "video" or filetype == "audio":
            return render_jinja("util/render_file.j2", filetype=filetype, file=subpath)

        # If it's a file, serve it for download
        return redirect(f"/raw_files/{subpath}")

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
    # When finding `semesterlist` values in the future, use the year but use the year + 1 if it is the fall semester.  XX is 00 for fall semester, 10 for spring semester, 20 for may term, 31 for summer term 1, and 32 for summer term 2.

    session = requests.Session()

    # Getting session cookies
    session.get("https://navigator.cnu.edu/StudentScheduleofClasses/socquery.aspx")

    # Defining the data to send
    # TODO: Parse __VIEWSTATE and __EVENTVALIDATION from bs4 output.
    data = {
        "__VIEWSTATE": "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",
        "__EVENTVALIDATION": "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",
        "semesterlist": "202700",
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

# Backend process for upgrading infuse player data
@app.post("/infusehelper")
def infusehelper():
    if "playerdata.yml" not in request.files:
        return "no playerdata", 404

    file = request.files["playerdata.yml"]

    # Reading the file
    data = file.read().decode("utf8")

    # Making the changes to the playerdata
    data = data.replace("§4Strength Effect", "strength")
    data = data.replace("§4Augmented Strength Effect", "aug_strength")
    data = data.replace("§eThunder Effect", "thunder")
    data = data.replace("§eAugmented Thunder Effect", "aug_thunder")
    data = data.replace("§#E8BD74Speed Effect", "speed")
    data = data.replace("§#E8BD74Augmented Speed Effect", "aug_speed")
    data = data.replace("§cRegeneration Effect", "regen")
    data = data.replace("§cAugmented Regeneration Effect", "aug_regen")
    data = data.replace("§9Ocean Effect", "ocean")
    data = data.replace("§9Augmented Ocean Effect", "aug_ocean")
    data = data.replace("§5Invisibility Effect", "invis")
    data = data.replace("§5Augmented Invisibility Effect", "aug_invis")
    data = data.replace("§cHeart Effect", "heart")
    data = data.replace("§cAugmented Heart Effect", "aug_heart")
    data = data.replace("§6Haste Effect", "haste")
    data = data.replace("§6Augmented Haste Effect", "aug_haste")
    data = data.replace("§bFrost Effect", "frost")
    data = data.replace("§bAugmented Frost Effect", "aug_frost")
    data = data.replace("§#E85720Fire Effect", "fire")
    data = data.replace("§#E85720Augmented Fire Effect", "aug_fire")
    data = data.replace("§#BEA3CAFeather Effect", "feather")
    data = data.replace("§#BEA3CAAugmented Feather Effect", "aug_feather")
    data = data.replace("§aEmerald Effect", "emerald")
    data = data.replace("§aAugmented Emerald Effect", "aug_emerald")
    data = data.replace("§5Ender Effect", "ender")
    data = data.replace("§5Augmented Ender Effect", "aug_ender")
    data = data.replace("§5Apophis Effect", "apophis")
    data = data.replace("§5Augmented Apophis Effect", "aug_apophis")
    data = data.lower()

    # Saving the playerdata to a file
    with open(".tmp/playerdata.yml", "w") as file:
        file.write(data)

    retval = send_from_directory(".tmp", "playerdata.yml")

    # Removing the file
    os.remove(".tmp/playerdata.yml")

    return retval

# Running the app
if __name__ == "__main__":
    app.run(debug=True, port=444, host="0.0.0.0")
