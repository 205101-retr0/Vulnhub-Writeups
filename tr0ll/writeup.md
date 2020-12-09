First as usual we run a nmap scan on the target.
We see 3 open ports 21, 22, 80.

The FTP port 21 allows Anonymous login.
logging into it we see there is a file lol.pcap. We download it onto our machine using the get command and open it in wireshark.

There we look at FTP-data where we see something like dir name called sup3rs3cr3tdirlol.
We try this dir on the webpage. We get a executable named roflmao.

Running that executable roflmao. We see it says "Find address 0x0856BF to proceed".

We put 0x0856BF in the webpage and see 2 more files there.

We get a list of users and password file. We can only assume this is for ssh login.

We try to bruteforce ssh login on this using hydra.

But the password in the pass.txt file doesn't give us anything but the dir said that we will find the password there.
So we try brute-force with Pass.txt as a password.

we get a match for user overflow.

__hydra -L which_one_lol.txt -p Pass.txt ssh://ip__.

We login to the server as overflow with password as Pass.txt

I poked around alot in the whole machine so we can looking for cronjobs in background.

We try to find a cronlog using : __find / -print 2>/dev/null | grep -e "cronlog"__

Inside the cronlog we see something being executed a file named cleaner.py

We try to find a that using : __find / -print 2>/dev/null | grep -e "cleaner.py"__

We see that cleaner.py runs as root so if we make a setuid binary and run it as root and spawn a shell, we'r done.

So we make a setuid binary root.c and change the code in cleaner.py to exec our binary.

cleaner.py --> 
os.system("chown root:root /tmp/root; chmod 4755 /tmp/root;")
<--

after that we wait for sometime and execute root.c 

To make root.c executable : __gcc -m32 root.c -o root__

So here chown changes the ownership of root.c so that it executes as root and chmod gives it setuid permissions.

After waiting sometime check if root.c has root ownership. When it does exec it.

And finally you will have the proof.txt file.