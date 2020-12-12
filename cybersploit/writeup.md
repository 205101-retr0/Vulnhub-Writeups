This is a fairly easy machine to hack.

Discover the machine's ip first using __arp-scan -l__.

After that running a nmap scan we see that there is only 2 ports here 22/ssh and 80/http.

Looking at the source code we see the comment telling us a username. This site has a robots.txt page, most of the wesites do, navigating over to that  we get the first flag.

I tried running a ssh brute-force using hydra and the username given to us in the source code but it gave me nothing.
So we can try the first flag we got as a trial and we got in. Brute-force was a waste of time.

After logging into the server alone we find the second flag. So that's done now the only thing left is to get root access.

We can search for exploitable setuid binaries or something but we and find nothing. So we can take a look the ubuntu and kernel version this machine is running.

__lsb_release -a__

Searching the ubuntu version on google we see that it's exploitable. And there is [code](https://www.exploit-db.com/exploits/37292) available for direct root priv esc on expoiltdb.

We can start a local http server using python server where we downloaded the priv esc code so that we can download it onto the vm.

__python3 -m http.server__

Now after downloading the code unto the vm server we just compile it and run it. And we will have root access and the final flag in /root directory. 

__gcc -m32 root.c -o root__

__./root__

EZ