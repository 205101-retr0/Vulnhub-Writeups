first do an nmap scan and we find that there is only one port (80 http). Now goto the site the login page, We see that it is a wp-login page.

We dont know the users so we enumerate the users using wpscan.

__wpscan --url http://ip --enumerate__

The site was made by a guy named cold so he must b the admin and we a user named c0ldd.

Now we do the dictionary attack on it using username as c0ldd.

__wpscan --url http://ip -U c0ldd -P /usr/share/wordlists/rockyou.txt__

we change the 404.php in themes and add a php reverse shell code there. Now we try trigger the error by checking out various links on the website.

When the error triggers we get a shell. Now we try for priv esc using setuid binaries and we try to locate if we have
anything we can use using : find / -prem -u=s -type f 2>/dev/null

we find the setuid binary /usr/bin/find.
It can be used to break out from restricted environments by spawning an interactive system shell. 
We can use this to get root access instantly.

search for [GTFObin find](https://gtfobins.github.io/gtfobins/find/). ./find . -exec  /bin/bash -p \; -quit

We goto /home/c0ldd and find user.txt which gives us flag 1.

NOTE : 
Before getting root access all login data is stored in wp-config.php file. 
The wp login file are all stored in var/www/html. There we can use :
cat wp-config.php | grep DB to get the creds of user c0ldd.
In the above scenario we got root access directly this is another way of going about it.
