A little bit tricky.

Firstly the nmap scan reveals only 2 ports 80/http, 22/ssh.

Looking at the source of website, a comment tells us not to waste time on robots.txt or scouting the source code.
So we run a gobuster scan to find any hidden directories.

There weren't any so we extend our search to hidden files. And we found one.

__gobuster dir -u target_ip -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .txt,.php,.html__

We find that /key.php we have to give in a key to get through no other way. We can a brute-force script for this but we can do it another way.

Running a nmap scan with --script and http enumeration we find another file.

__nmap -sS -sC --script=http-enum -p 80 target_ip__

Running this command we a file, navigating to that on website. we get a rsa key and the title to that page can be the username to ssh.

We copy the contents of the rsa file onto our system and give it permissions.

__chmod 600 rsa_id__

Now we can login to the server as mpampis.

__ssh -i rsa_id mpampis@target_ip__.

There we got the first flag after logging in.

We have no information after this on how to proceed to i tried if there are any setuid binaries we can use but there are none. 
So we try __sudo -l__ to see what we can run as root.

Turns out we can use /usr/share/gcc as root. So we can directly get a root shell using this.

We can copy this sudo command from [GTFObins](https://gtfobins.github.io/gtfobins/gcc/).

Just navigate over to /usr/share and run:

__sudo gcc -wrapper /bin/sh,-s .__

And there we are logged in as root.