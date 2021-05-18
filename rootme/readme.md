Easy TryHackMe box called RootMe.

`Machine ip:  10.10.209.234`

`open ports(nmap scan):
basic -sV -sC -T4
22
80
`

`Hidden Dirs(gobuster search):
uploads               ## prolly a reverse shell exploit. 
panel 				  ## Login panel
`

upload file type was only .png 
so mv shell.php shell.phtml
and trigger it.

`Priv esc:
/usr/bin/python -- setuid
gtfobins
`

Note: Very Very Very bad shell to control