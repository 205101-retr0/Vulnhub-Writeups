Note: This machine works better in vmware.

The ip of the machine is available on the machine itself so We jump to directly to nmap scan.
Running dirb to find the hidden dirs we find a dir called /joomla.
We goto /joomla/administrator to get the login form.
But first we have to generate a wordlist for the brute-force of users.
There is no way of enumerating users in joomla login so we try and guess the users.

__cewl -m 6 http://host_ip/joomla/ >> dic.txt__ --> for dictionary attack.

Now we use burp-suite intruder to execute a dictionary attack with usernames like admin, administrator, joomla etc...

luckily we get a match for joomla:Gotham.

Now here we can put in a php-reverse-shell code in the style-templates and hit template-preview to trigger it.

We keep listening on the mentioned port in the reverse shell code. Hence, we get a shell there.

Go ahead and check the config file if we can find some sql dbs.

going to var/www/html/joomla. We a file called config.php. Going thru that we find username and password to a mysql db.

__joomla:babyjoker__ --> creds for the mysql db.

Logging to the database using the creds and listing the dbs. We get there is a db called batjoke.

Looking at the tables there is one called taskforce. They are the creds to login to server using ssh.

Trying them all only one works.

_*MYSQL COMMANDS*_

__show databases;__

__use \<database>;__

__show tables;__

__select * from \<table>;__

__rob:???AllIHaveAreNegativeThoughts???__ --> creds to ssh login into glassglow server.

After logging into the server, We get our first flag.

Here, there is a abner text file that seems encrypted. It's rot 1 encryption. Decoding that we get password for the user abner.

Now, we can login as abner and get the second flag. In this dir, there is a info.txt file which is completely useless.

So we use ls -la and take a look at .bash_history. We see a zip file called dear_penguin. We can search for it using find command.

__find -print 2>/dev/null | grep -e "dear_penguins.zip"__ 

Unzip it using the same login password and we get a text file which contains the password to user penguin.

cd into the dir and we find the third flag.

Now for the final root flag.

We can't use the setuid find here as it can be only used by root user. So that's a rabbit hole.

But using ls -la we can see a .trash_old exec file.

Now this bit was hard. snooping around I could nothing so I used [pspy](https://github.com/DominicBreuker/pspy).

We can download it from the downloads dir onto the server using : __scp pspy64 penguin@192.168.148.128:/home/penguin__.

Running this for some time we see:
```
  CMD: UID=0    PID=1618   | /usr/sbin/CRON -f 
  CMD: UID=0    PID=1619   | /bin/sh -c /home/penguin/SomeoneWhoHidesBehindAMask/.trash_old
   ```

This means .old_trash is running on cron timely. We can add a nc reverse-shell to that file and keep listening on that port to get a root shell.

After waiting for sometime we get a shell.

And we get the root flag finally.
