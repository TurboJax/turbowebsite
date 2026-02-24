TribeCTF 2025 Challenges
TribeCTF 2025 Challenges
## The First Flag
> Every flag in this competition follows the format tribectf{super\_secret\_flag}.  
> Your mission for each challenge is to discover and submit the flag. But before you dive in, there's something you must do: read the rules.  
> Head to [this link](https://turbojax.org/ctf_rules.html), and comb through it carefully.  You might just uncover your first flag hidden within.

## Coworkers
> Look at Griffin's letter—he shares his coworkers favorite numbers and a fun song he learned.  
>   
> **FILES:**  
> - [msg.txt](https://turbojax.org/static/ctfthings/msg.txt)

## pytryoshka
> Sticky Nicky has been at it again, stealing office supplies from the Computer Science department to sell on the lucrative office supplies black market. Hidden somewhere inside this python file is the password for the vault. Can you find it so all the professors can have their pens and paper back?  
>   
> **FILES:**  
> - [level_2.py](https://turbojax.org/static/ctfthings/level_2.py)

## Case Manager
> You have come upon a unique historical artifact: the proprietary Case Management executable once used by the law firm of Thomas Jefferson and his associates way back in the days.  
> Examine this piece of colonial software and retrieve the flag, proving your access to the firm's most secret dealings.  
>   
> **FILES:**  
> - [Case_Manager.zip](https://turbojax.org/static/ctfthings/Case_Manager.zip)

## Contact Form
> The law firm of Thomas Jefferson and his associates is famously preoccupied, deep in historical cases and unavailable for commentary.  
> You have critical, time-sensitive information they need, but their lines are locked down. Fortunately, you've located a strange, ancient binary that contains all of their private contact and availability data.  
> Can you uncover the secrets within this historical artifact and retrieve the flag?  
>   
> **FILES:**  
> - [ContactForm](https://turbojax.org/static/ctfthings/ContactForm)

## Jeff's Screensaver
> We think there is a hidden message in Jeff's Screensaver. Find it.  
>   
> **FILES:**  
> - [ScreensaverJeff](https://turbojax.org/static/ctfthings/ScreensaverJeff)

## Dig me up!
> The royal cypher lies buried in our archives. Some secrets are written in stone, others in text. Can you unearth what's hidden?  
> Server: `35.227.52.228` Port: `1053`  

## Ducker Hunt
> The ducks of Williamsburg hide more than feathers—take aim and see if you can bag the flag.  
>   
> **FILES:**  
> - [ducker-hunt.tar](https://turbojax.org/static/ctfthings/ducker-hunt.tar)

## Key Witness
> Jeff's been acting strange lately, and his online habits are even stranger. We've been watching and have a snapshot of his network activity for you to analyze. Find out what he's trying to hide.  
>   
> **FILES:**  
> - [WorkComputerInputs.pcapng](https://turbojax.org/static/ctfthings/WorkComputerInputs.pcapng)
> - [WorkComputerNetworkTraffic.pcapng](https://turbojax.org/static/ctfthings/WorkComputerNetworkTraffic.pcapng)

## Sir Wren Sings!
> This knighted architect keeps watch over the yard, whispering an anthem older than your grand-grandparents.  
> Legend says Wren himself left a clue for those who listen closely - start where the winds sing, or maybe where the shells shout.  
>   
> **FILES:**  
> - [sir_wren_sings.jpg](https://turbojax.org/static/ctfthings/sir_wren_sings.jpg)

## Not So Top Secret Vault
> Mission Briefing  
> Congratulations, agent. You've successfully gained access to a server containing a sensitive vault application. Our intelligence suggests this system stores classified information that could be crucial to our mission.  
> The Situation  
> Initial reconnaissance reveals:  
> The target deployed an encrypted note vault application  
> Someone on their dev team decided to "vibe code" this security-critical application  
> Poor development practices may have left vulnerabilities we can exploit  
> curl 128.239.26.203:5000  

## Ready, Set, Go!
> You are provided with the code of a simple HTTP server running on the server. It accepts file_name as a query parameter and responds with the contents of that file.  
> First, start the challenge Docker container and use curl to connect to challenge's IP and port.  
> Docker Container Information:  
> Host: 128.239.26.203 Port: 38764/tcp  
>   
> **FILES:**  
> - [ready_set_go_src.zip](https://turbojax.org/static/ctfthings/ready_set_go_src.zip)

## case_request
> The W&M parking authority keeps giving you tickets. You are trying to appeal your ticket online so that they will refund your student account.  
> Fill out the form to check whether your claim is refunded. To run the site, use python3 -m http.server or a similar program in the site/ directory.  
>   
> **FILES:**  
> - [case_request.zip](https://turbojax.org/static/ctfthings/case_request.zip)

## mindpq
> British spies collected 100 samples of communications from the Continental Army. Each sample consists of an RSA public key, and a message encrypted with that key.  
> For instance, key-0.pem encrypts the message ct-0.bin, key-1.pem encrypts ct-1.bin, and so on. Your intelligence sources indicate that the Continental Army is not adept at key management.  
> While you won't be able to decrypt all messages, your intuition tells you that you might be able to leverage these weaknesses to decrypt a few.  
> Your goal is to decrypt a few of the messages; the flag is the concatenation of the resultant plaintexts.  
> Hints:  
> - The RSA keys use a 1024-bit modulus  
> - The .pem files are PEM encodings of PKCS #1, ASN.1 DER form  
> - RSA encryption uses the PKCS1 #1 v1.5 padding scheme  
>   
> **FILES:**  
> - [mindpq.zip](https://turbojax.org/static/ctfthings/mindpq.zip)

## rngcrack
> Thomas Jefferson is communicating with founding fathers Langdon, Carroll, and Gilman using their so-called "LCG"-based encrypted messaging system.  
> The cryptosystem consists of a pseudo-random number generator that produces integers x\_1, x\_2, x\_3, ... Let m\_i be the ith message.  
> To encrypt m\_i, the founding fathers pass the string version of x\_i to SHA-256, producing an AES-256 key, k\_i.  
> The founders then use AES-256 in CTR mode to encrypt m\_i with k\_i. For instance, if x\_i is 13374567, then, k\_i is the SHA256 of the eight bytes "13374567".  
> British spies have captured the first 1000 numbers of the pseudo-random number generator (stream.dat), along with the a message (ciphertext.bin) encrypted with its next random number (the 1001st).  
> Your goal is to determine the value of this 1001st random number and decrypt the message.  
> HT: The IV is hex aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  
>   
> **FILES:**  
> - [rngcrack.zip](https://turbojax.org/static/ctfthings/rngcrack.zip)

## GOPR
> The William & Mary Griffin Platforms Lab (GPL) inherited a dusty development board from a decommissioned AI initiative known only by its codename WOPR.  
> The project team originally built WOPR to experiment with early decision-making heuristics and on-device learning, but the project was abruptly archived and the documentation scrubbed.  
> During a routine inventory, the lab's custodial AI booted the device enough to reveal a single taunting message: “Do you want to play a game?”  
> The only thing left from the original development notes is a single file flash.img. No one knows what it is.  
> Your team has been tasked with exploring the WOPR project's old secrets and unraveling the mysteries of its game.  
> nc 128.239.26.203 4000  
>   
> **FILES:**  
> - [flash.img](https://turbojax.org/static/ctfthings/flash.img)

## Griffin's Game
> While exploring the archives of the WOPR project, William & Mary's Griffin Platforms Lab (GPL) found a network hidden in plain sight for their GOPR project.  
> A series of hidden devices designed as a failsafe for the project. Nicknamed the "4 Horsemen of the Apocalypse" the network served to shutdown GOPR should it go rouge.  
> However, when GOPR went rouge, it took over the network and formed a game, Griffin's Game. Your mission should you choose to accept it, is to find the hidden network and solve Griffin's Game.  
> Note: Place the flag into the tribectf{} format and seperate full words by underscores.  

## logic_level
> During cataloging of the archived WOPR project, William & Mary's Griffin Platforms Lab (GPL) found an old schematic for a custom digital circuit used in the AI's decision-logic experiments.  
> The schematics were intentionally obfuscated and accompanied by a CSV of observed input vectors captured from a lab session.  
> The custodial AI left one message on the schematic's margin: “Derive the outputs — then read the flag.”  
> Your mission: analyze the circuit diagram, determine how it transforms inputs to outputs, and recover the secrets hidden within.  
>   
> **FILES:**  
> - [LogicLevel.pdf](https://turbojax.org/static/ctfthings/LogicLevel.pdf)
> - [streams.csv](https://turbojax.org/static/ctfthings/streams.csv)
