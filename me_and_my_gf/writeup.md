The nmap scan on the target reveals two ports 22/tcp ssh and 80/http.
Going to the website and trying to register as user it shows us a message.

"Who are you? Hacker? Sorry This Site Can Only Be Accessed local!"

Looking at the source code we get a hint to use x-forwarded-for.

It is a chrome extension and be basically used to change the current ip address for sometime so that the target's server thinks it's local.

Now we can register as a user. After that we go to the profile page cause we want see if we can find other people.
In the url __http://target_ip/index.php?page=profile&user_id=12__ we see this thing called user_id.

If we change the user_id we can see that the username and password change too. We can look at the values by looking at the source code of the page. We can the user_id to 1 and get the credentials to ssh login.

Now we navigate over to /var/www/html to see if there is any config file. And there is.

There we find the creds to root user.

we can switch to root using: __su root__.

Now we navigate over to user alice and find her secret as a hidden file. And we have root access so we can go to the root directory and read the root flag too.

NOTE: If we wanted to find everyone's user credentials then we can just login into the mysql using the root creds
      __mysql -u root -p__.
      
      MYSQL COMMANDS:
      
      __show databases;__
      
      __use < db >;__
      
      __show tables;__
      
      __select * from < table >;__
