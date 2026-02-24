TribeCTF 2025 Writeup
TribeCTF 2025 Writeup
## Key Witness
> The challenge gives us two pcap files.  One is Jeff's network traffic, the other is a monitoring of his USB keyboard inputs.  
> Inspecting the network traffic, you can see he visits a file server with 4 files uploaded to it (Captures 25 and 29).  Three are motivational cat pictures, the fourth is a zip file named "SuperSecretStash.zip"  
> Eventually, he downloads the SuperSecretStash.zip file (Captures 635 and 639), allowing you to export it to your system by right clicking the "Media type" dropdown and selecting the "Export Packet Bytes" option.  
> Unfortunately, it's password protected, which is where the USB pcap comes in.  
> Since we have the USB pcap, we basically have a keylogger we can use to find what Jeff's password to the zip file is.  
> All of the URB_INTERRUPT packets are keys being pressed on Jeff's keyboard.  To make it easier to export the data, I used tshark (terminal wireshark) and ran this command to get the keycodes into a manageable format.  
> `tshark -r WorkComputerInputs.pcapng -T fields -e usb.capdata > keys.txt`  
> With this data, I went online to find a script that could convert the codes to text, linked [here](https://blog.stayontarget.org/2019/03/decoding-mixed-case-usb-keystrokes-from.html)  
> The file required slight modifications due to it not handling empty lines of input well, but I managed to fix it by adding an if statement that skipped the line if the length of the "bytesArray" variable was less than 3.
> It printed out this string: `COLESspaceEVILspaceDIARYEnter-plansspaceforspacetoday-EnterDefraudspaceMackEnterStealspaceclientspacedataEnterSellspaceclientspacedataEnterEnterDOspaceNOTspaceFORGETspacePASSWORDEnterC0l3S_3V1l-p1aNEnterEnterColesspaceprospacetipEnter7zipspaceseemsspacetospaceworkspaceforspaceextraction`
> Which I could convert to: 
```
COLES EVIL DIARY
-plans for today-
Defraud Mack
Steal client data
Sell client data

DO NOT FORGET PASSWORD
C0l3S_3V1l-p1aN

Coles pro tip
7zip seems to work for extraction
```
> Using the password mentioned in the keyboard inputs, `C0l3S_3V1l-p1aN`, I was able to open the zip file.
> Inside the zip file was a file called "StolenUserData", and inside it was the flag `tribectf{w1R3Sh4rK_1s_4_p0W3RFul_100l_}`

## Sir Wren Sings!
> The challenge gives us [this jpg](https://turbojax.org/static/ctfs/tribectf_2025/sir_wren_sings.jpg) of a famous architect.  This challenge can be solved by going to [https://www.aperisolve.com/](https://www.aperisolve.com/), uploading the file, and scrolling through the output.  
> You may notice the random string of characters in the "comment" tag in the exiftool output.  A quick hop over to dcode.fr's [cipher identier](https://www.dcode.fr/cipher-identifier) reveals that the text may be base64 ecnoded.  
> When you enter the code into a base64 decoder, you'll get the flag, which is `tribeCTF{"hack_upon_the_flag"}`  

## The First Flag -- SOLVABLE
## Coworkers -- SOLVABLE
## pytryoshka -- SOLVABLE
## Case Manager -- SOLVABLE
## Contact Form -- SOLVABLE
## Jeff's Screensaver -- SOLVABLE
## Dig me up! -- UNSOLVABLE
## Ducker Hunt -- SOLVED
## Not So Top Secret Vault -- UNSOLVABLE
## Ready, Set, Go! -- SOLVABLE
## case_request -- SOLVABLE
## mindpq -- SOLVABLE
## rngcrack -- SOLVABLE
## GOPR -- SOLVABLE?
## Griffin's Game -- UNSOLVABLE
## logic_level -- SOLVABLE
