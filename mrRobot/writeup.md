This machine has a very interactive website. That's a big rabbit hole. There is nothing there.

First we do a nmap scan and discover that the open ports are 22-ssh, 80-http, 443-ssl.

Running a dirb scan on website we see a robots.txt file and wordpress files too.

Going to robots.txt we find our first flag and fsocity.dic dcitionary file.

This can be used to brute-force the users and passwords of wordpress login.

We enumerate the users using hydra. And it's a little complex here because we need to post the data and catch the Invalid password result only.

We can see the name of the username and password fields just by looking at the source code of the login site.

__hydra -U fsocity.dic -p test host_ip http-post-form:"/wp-login.php:log=^USER^&pwd=^PASS^:Invalid".__

Running this we get a match for username as Elliot.

Now we can run a brute-force dictionary attack using this username and fsocity.dic

__wpscan --url http://host_ip -U Elliot -P fsocity.dic__ 

This is gonna take a long time cause the password is a bit further down. atleast 30 minutes depending upon the processor.

After logging we can change the 404.php in themes editor to a php reverse shell. 
Start listening on the port u put in the php reverse shell.
And trigger E404 to catch a shell.

We can goto /home/robot but we can't read flag 2 untill we login as user robot. But there is another file named password which is a raw-md5 hash.

we can crack it online using this [site](https://crackstation.net/) or We can use john the ripper to crack the password hash.

The password comes out to be __robot : abcdefghijklmnopqrstuvwxyz__

Now we can switch to user robot using __su - robot__

There we have our second flag.
For the third flag we try use setuid binary running with root permission.

To find the binaries we use the find command.

__find / -user root -perm /4000 -type f 2>/dev/null__

We see /usr/local/bin/nmap. We can run nmap interactive mode to run it as root.

__nmap --interactive__

__nmap>!sh__

There we have a root shell. We can go and read the root or third flag.