First we locate the target using arp-scan.
After that we run a nmap scan on it. There we discover 3 ports 3 http and 1 ssh.

The website with deafult port value didn't have anything. So we turn our attention towards the one with port 31337.

Looking at the source there we find bas64 text which decoded gives us a filename Cypher.matrix

Putting that into the url it directly downloads a file. Opening it we see it's brainfuck language.

Decoding that we that the password of the guest user is K1ll0rXX where XX is unknown. So we generate a dictionary.

The dictionary will contain all possible combinations of XX with ascii and integers added after K1ll0r. Now using this dictionary we can use hydra to launch an attack on ssh port.

__hydra -l guest -P dic.txt ssh://target_ip__

After this runs we login to the machine as guest. But we see that we cant anything commands.

Only working command was the echo command which can be used to look into the directories.

We do __echo *__ to list all the dirs. There is one dir called prog. We can do __echo prog/*__ to look into that.

There we see that there is a file vi. So we can use vim editor. We can use that to get a bash shell.

In the vim editor : ___:!/bin/bash___ 
Now we have a bash shell but we can't run sudo so we can't sudousers commands.

We have to set a path variable to run all sudo command. That will be __PATH=/usr/bin:/bin/__.

Now we can use sudo -l to see what we can use here as guest. We see that we can use all commands as guest meaning we can just use __sudo -i__ and type in the password to get root access.

There we can read the flag now.