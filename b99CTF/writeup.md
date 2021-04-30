This is an easy box from TryHackMe.

Anonymous FTP login revealed that the password was easy to crack. So we can use hydra to brute-force it with username jake.

_hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://Machine_ip_

___Username: jake Password: 987654321___

After logging in as jake we can't find the user flag. After digging around a bit you can see that it's in /home/Holt 
and it has read permissions by jake so we can read it right now.

__User Flag: ee11cbb19052e40b07aac0ca060c23ee__

Now that we're in the box we can start with priv esc. running the sudo -l command we get that all users can run the less command.

/usr/bin/less --> if we run this as sudo we can get root access easily.

We can either use [GTFObins for sudo using less](https://gtfobins.github.io/gtfobins/less/)

Open any random or new file using the less command and then just type in the command line area: _!/bin/bash_

And there we have it. The box is rooted.

__Root Flag: 63a9f0ea7bb98050796b649e85481845__