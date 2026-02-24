CYBR 198 Challenges
CYBR 198 Challenges
Resolution Over Isotopes  
> numeric value to 3 decimal places  
> big num / small num  
> 1.6 (searched for "pixel")  
> 235 or 238 (searched for "U-")  
> Tried both 235/1.6 and 238/1.6  
> 235/1.6 worked, the answer was "146.875"  

s0me Simple Ma7h  
> The answer is the value of (number that describes the exploit) * (version number of the OS) as a word  
> Maybe cve?  CVE # is "CVE-2010-2772"  
> Reading chapter 1, the windows version number might be "7", but it attacked upwards of windows 2000  
> I overthought this...  It's a **zero**-day exploit.  The number that describes it is "0"  
> The answer is "zero"  

Eyes and Ocean servers  
> I searched for "stuxnet" on the document and went until I found the domains.  
> The answer was "mypremierfutbol.com,todaysfutbol.com"  

The one encoded Royal Flush of Spades  
> one encoded references "Unicode"  
> Playing cards have unicode values.  
> "ascend" because the cards need to be in ascending order.  
> Answer is: "🂪🂫🂭🂮🂡"  

The long and Short of it  
> . -. -.-. --- -.. . -.. / ..-. .-.. .- --.  
> Translates to "ENCODED FLAG"  
> Tried that, didn't work.  
> Turns out I had an error because my translator put its output in all caps.  
> I tried "encoded flag", and it worked!  

Decoding the Digital Trail  
> bunch of binary:  
> "01000011 01001110 01010101 01011111 01000011 01111001 01100010 00110011 01110010 01011111 01010010 00110000 01100011 01101011 01110011 00100001"  
> Translates to "CNU_Cyb3r_R0cks!", which was the flag.  

Encoded Traces  
> Gave me a string:  
> "SGFjazNyc19VczNfVGgxc19NM3RoMGRfQWxsX1RoM19UMW0z"  
> Went to dcode.fr/en to check their cipher identifier.  
> First result was base64, so I added two equals signs (=)  to the end and got this:  
> "Hack3rs_Us3_Th1s_M3th0d_All_Th3_T1m3", which was the flag.  

\[Encoding\]🐍👀  
> Googled the emojis, and it mentioned snake eyes, a thing that you would roll on a dice.  
> Remembering the unicode royal flush, I looked for the unicode for a one on a dice, "⚀"  
> The answer was "⚀⚀" since it was snake eyes.  

P Ell Seas  
> I searched for "logic controller" in the book, and found this quote:  
> "the company’s S7-315 and S7-417 programmable logic controllers."  
> 417-315=102, which was the answer.  

Getting your Digital Shots  
> I searched for "inoculation", and found the specific value stuxnet used in the footnotes on page 175.  
> The value was "0x19790509", which was the answer.  

Scrabble  
> Mentions the Melissa virus.  I searched "Melissa" in the book and found that it mentioned "twenty-two, plus triple-word-score, plus fifty points for using all my letters. Game’s over. I’m outta here."  
> 22\*3+50=116, which was the flag  

Centerfuge Hall  
> How many centrifuges could've fit in the 32000 square meter halls at Natanz?  
> Searched the book for "Natanz", and found the number "47000" on page 51.  
> This somehow wasn't the flag.  I tried "47,000", "47000", "47,000 centrifuges", and "47000 centrifuges".  
> I also went to the wayback machine to view the linked analysis of the site, and tried "50,000", "50000", "50,000 centrifuges", and "50000 centrifuges" based on what was there.  
> Dont know this one  
> The answer was "94000" because it was 47000 \* 2 thanks to there being two halls.  

End of the Year?  
> I searched for "2007", and one of the quotes mentioned "3000".  
> "3000" was the flag.  

Weapons Grade  
> I searched for "weapons-grade", and found that it needed 90 percent enrichment on page 234.  
> The flag was "90".  

INSPECTor Gadget  
> I went to the provided link: [http://cybr198.com/inspectorgadget.html](http://cybr198.com/inspectorgadget.html) and pressed f12 to view the page's source code.  
> I saw a comment with "flag{youfoundme}" inside it.  I entered "youfoundme" into the box, and it worked.  

What Percent of the 1 of the five?  
> I searched for "percent", and one of the footnotes mentioned one exploit being 69% of the attack.  "69" was the answer.  

How many Zeros?  
> Searched for "zero-day", and found the result on page 180.  
> answer was "5"  

How many Copies?  
> Searched for "copies", and found the result on page 65.  
> answer was "3280  

Wavy Message  
> Mentioned "rails", went to dcode.fr and searched "rails".  Found the rail fence cipher.  Put the ciphertext in, hit automatic decryption, and found the answer "DECODEME"  

\[W6\] Oh Ceasar - My S4lad!  
> Caesar cipher  
> dcode.fr gave "simplecipher"  

The Secret Code  
> I got a random string of numbers, which made me think of ascii.  
> The string was "70 76 65 71 123 97 115 99 49 49 95 118 52 108 117 51 115 95 97 114 51 95 107 51 121 125"  
> Decoding the string from decimal to ascii gave me "FLAG{asc11_v4lu3s_ar3_k3y}"  

The Corrupted File  
> Opening the attached file, I see a string that looks like base64 due to the equals sign at the end of the string.  
> String is "VGhlIHN1c3BlY3Qgd2FzIHNlZW4gYWNjZXNzaW5nIHRoZSBzZXJ2ZXIgcm9vbSBhdCAyMzozMCBvbiBTZXB0ZW1iZXIgMTR0aC4KClNlY3VyaXR5IGZvb3RhZ2Ugc2hvd3M6Ci0gVW5hdXRob3JpemVkIGFjY2VzcyB0byBTZXJ2ZXIgUmFjayAjNwotIFVTQiBkZXZpY2UgY29ubmVjdGVkIGZvciA3IG1pbnV0ZXMKLSBGaWxlIHRyYW5zZmVyIGRldGVjdGVkOiB+MzUwTUIKClRoZSBleGZpbHRyYXRlZCBkYXRhIGluY2x1ZGVkOgoxLiBDdXN0b21lciBkYXRhYmFzZSAoZW5jcnlwdGVkKQoyLiBFbXBsb3llZSByZWNvcmRzCjMuIEZpbmFuY2lhbCByZXBvcnRzIFEzIDIwMjQKCkZMQUc6IEZMQUd7YjRzMzY0X2lzX24wdF9lbmNyeXB0MTBufQoKQWRkaXRpb25hbCBOb3RlczoKVGhlIHN1c3BlY3QncyBsYXB0b3Agc2hvd2VkIHNpZ25zIG9mIGFudGktZm9yZW5zaWNzIHRvb2xzLgpCcm93c2VyIGhpc3Rvcnkgd2FzIHdpcGVkIHVzaW5nIENDbGVhbmVyLgpFbWFpbCBjb3JyZXNwb25kZW5jZSB3aXRoIHVua25vd24gcGFydGllcyBmb3VuZC4="  
> Decoding it from base64 gave me a message, in the middle was a flag.  
> The flag was "FLAG{b4s364_is_n0t_encrypt10n}"  

\[W7\]Check the Latitude at the door!  
> The challenge mentions "exif", so time to upload the image to [exif.tools](https://exif.tools).  
> The challenge is to get the whole number and the lowercase letter representing the direction, which becomes "67n"  

SFBM's Caesar Salad  
> Got a morse string, decrypted it.  Then put it through a caesar cipher, and got the result "LOOKINGDEEPER".  Converting it to lowercase is "lookingdeeper", which was the answer.  

What park where?  
> The answer was "Pyhä-Luoston kansallispuisto"  
> There are TOO MANY VARIATIONS OF THE KEY.  

(Hacker) Man in the Middle  
> Searched the book for "middle", and the it was on the first page with results.  Answer was "The Grugq"  

Endgame?  
> Searched for "endgame" and found the results on pages 72 and 73.  
> Answer was "Cayman,Corsica,Maui"  

The Highs and Lows of Browser Holes  
> Searched for "Browser" and found a range on page 69.  "$60,000 to more than $200,000"  
> Answer was "60000-200000"  

Stepping Stones to Where?  
> Searched for "PLC".  Found the two PLC model numbers on page 109, and found the software used to program them on page 109 as well.  
> Versions were "S7-315" and "S7-417", and the number in the software was "7".  
> 315+417+7=739.  
> Answer was "739"  

German Counterpart  
> Searched for "response team" and found "CERT-Bund" on page 110.  
> Answer was "CERT-Bund" (case sensitive)  

How do you say it?  
> Searched for "NCCIC" and found the pronunciation on page 119.  
> Answer was "N-Kick"  

Put it in reverse Terry!  
> given a message and a photo. Message: "fixe eht dnif - tnemmoc resu eht dnif dluoc uoy ylno fi"  
> Reversed it reads: "if only you could find the user comment - find the exif".  
> Uploaded the file to https://exif.tools and found "-.. . -.. --- -.-. -. . . .-.. .--. .. .-. -" in the comments.  
> Converting that from binary yielded "dedocneelpirt"  
> Reversed, this is "tripleencoded", which was the answer  

BitENCendo 64  
> Given a base64 string "dHdvdG90aGVzaXh0aA\=\=" (assumed base64 due to the equals signs)  
> decodes to "twotothesixth", which is the flag.  

Time for goodbyes  
> Searched for "KGB", and it was listed on the first page of results.  
> The key was "Farewell Dossier"  

It's not magic, or is it?  
> Searched for "315", and found it on page 148.  
> Listed "2C CB 00 01, 7050h, and 9500h"  
> Formatting it to follow the challege, it became "2CCB0001,7050h,9500h".  
> This was the key.  

Friend or Foe  
> Searched for "Boldi" and found the hash he posted on page 164.  
> The key should've been "ee87ec", but a typo was made and it was actually the last 7 characters, not 6.  This turned the key to "9ee87ec"  

To the Stars!  
> Searched for "keylogger", and found the mentions of images on page 168.  
> The "title of the image" wasn't referenced, but some text was mentioned, which was "Interacting Galaxy System NGC 6745".  The book had a period in the quotes, but the key didn't take it.  

What Day?  
> Searched for "mcafee" and found the key on page 168.  It mentioned an article written by Peter Szor titled "The Day of the Golden Jackal", which was the key.  

what is coming?  
> Searched for "Cyberwar ", including the space to prevent getting words like "cyberwarfare".  Found the answer on page 134, which mentions when the word was coined.  The book says the term was coined in 1993 by RAND, so they key was "1993 RAND"  

Vignere  
> Given a message and a string "whatcouldthecodewordbe"  
> Using the string as the code word, I decrypted the text to "polyalphabetcode" using dcode.fr  
> This was the flag  

Baby Shark...  
> Got a .pcap file, time for Wireshark.  
> Told to look for the IP of the host with the MAC address "00:50:56:ed:c2:e2".  
> The first entry says the destination address has the mac address we're looking for, and that IP is "192.168.28.2"  
> This was the flag.  

samuelfbmorse vignere ceasar s4lad  
> Given morse code  
> Mentions vignere and caesar ciphers, so i'll have to run through both  
> Guessing the vignere key is "samuelfb", a random string in the title  
> Got the string "tripleencoded", which was the key  

2007  
> Given a video.  It's a link to Rick Astley's Never Gonna Give You Up.  
> "Never Gonna Give You Up" was the key  

SecureBank  
> Told to look for creds in the source code.  This was in a \<script\> tag on the bottom of the page.  
> Username "admin" password "sup3rS3cur3P@ss"  
> Entering the info gave the flag "flag{insp3ct_3l3m3nts_f0und_15}"  

robots.txt  
> Given a link to a website.  
> Robots.txt is a file that is intended to tell bots where not to go, but can often reveal locations on the page.  
> Adding "/robots.txt" to the url shows the file, and it contains a single path, "/sekrits/".  Going there, I found the flag "flag{butwhereartherobots?}"  

,tmp  
> Searched for ".tmp" and found "~DF78.tmp" and "~DEB93D.tmp".  Formatting like the prompt asks, the flag became "~DEB93D.tmp~DF78.tmp".  

How Long?  
> Searched for "days" from the beginning of chapter 16.  I see mentions of "35" and "298", so the flag is "35 298"  

1st Max Speed? (UNSOLVED BY ME)  
> Found the numbers by searching "hz" from the start of chapter 17.  
> There was an error with the formatting, and rather than check with the teacher I maxed out my attempts, try one of the following:  
> "1,410 1,324 1,381"  
> "1410 1324 1381"  

GETting to the bottom of the HTTP password?  
> Found a part of the request url that had a plaintext, unencrypted "password" field.  The password was "insecur3-http"  

Base128 (Crypto)  
> Given an encrypted string "Wm14aFozdFVhREZ6WHpFMVgzZG9lVjkzTTE5MU5XVmZjM1J5TUc1bk0zSmZNMjVqY25sd2RERXdibjBLCg\=\="  
> Base128 encoding is a thing, but putting it through that gave gibberish.  
> Base64 is more popular, and I did get all ascii characters from doing it once.  
> Doing it a second time (64\*2 = 128), gave me the flag "flag{Th1s_15_why_w3_u5e_str0ng3r_3ncrypt10n}".  

Ask who? (Crypto)  
> Given a list of numbers, I'm thinking ascii.  
> With a conversion from decimal to ascii, I get the decoded string "The password is 689b40f6be97b62b5be6".  The flag was "689b40f6be97b62b5be6".  

\'dem bones (Crypto)  
> Given an image with the text "gvovn be abg gvovn"  
> Trying caesar cipher bc it's a simple cipher.  Got "tibia or not tibia".  This was the key.  

Eye End Ere (Crypto)  
> Image mentions a key being "EYESPY"  
> Using the "strings" cli tool, I found a base64 encrypted string "WW91J3JlIGFsbW9zdCB0aGVyZS4uLiBqamV5e2NteF95cG9wd3dfZ3JfbHdjX21rZXl0fQ\=\="  
> Decrypting that gave "You're almost there... jjey{cmx_ypopww_gr_lwc_mkeyt}"  
> Using the vignere cipher with the "EYESPY" key, I got "flag{not_always_in_the_image}"  

I am Grep (Forensics)  
> So it's a large file, but I kinda opened it and saw the flag immediately.  
> You are intended to use the grep command to search for the keyword "flag", or search for it with a gui.  
> The flag is "THIS-IS_THE-FLAG{grep_and_you_will_find_42783683}"  
