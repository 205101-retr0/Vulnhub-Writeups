First we discover the ip of the machine using __arp-scan -l__.

We then run an nmap scan on the target and that reveals we have 4 ports open 22/ssh, 80/http, 8008/http, 65534/ftp.

__nmap -p- target_ip__.

__nmap -sS -sC target_ip__.

Trying robots.txt on the webserver we got our first flag.

Looking at the source code of 80/http we can see a convo between 2 employees of the company in the comments. Going to the video in the comments. I check out the video and see that we're being pointed to prehistoric forest.

```
<!--Comment from Nick: backup copy is in Big Tom's home folder-->
<!--Comment from Richard: can you give me access too? Big Tom's the only one w/password-->
<!--Comment from Nick: Yeah yeah, my processor can only handle one command at a time-->
<!--Comment from Richard: please, I'll ask nicely-->
<!--Comment from Nick: I will set you up with admin access *if* you tell Tom to stop storing important information in the company blog-->
<!--Comment from Richard: Deal.  Where's the blog again?-->
<!--Comment from Nick: Seriously? You losers are hopeless. We hid it in a folder named after the place you noticed after you and Tom Jr. had your big fight. You know, where you cracked him over the head with a board. It's here if you don't remember: https://www.youtube.com/watch?v=VUxOd4CszJ8--> 
<!--Comment from Richard: Ah! How could I forget?  Thanks-->
```
So we navigate over to /prehistoricforest on the web server. We see its a wordpress site.

I start reading some of the blog posts and find the second flag! It's a comment by Michelle Michelle on Announcing the Callahan internal company blog!"

In the posts we can a post SON OF A! which seems interesting so we go check it out.

And we get another dir to navigate to. /richard. We will also have to enumerate the users and bruteforce the passwords for this wordpress site.

But for now we get an image so there might be some steganography involed. So we can take a look at the exif data of the image for now.

__exiftool shocker.jpg__

In the user comments we have a md-5 hash which can be cracked using john the ripper or some [online hash cracker](https://crackstation.net/).

The decoded hash comes out to be ___spanky___.

This might the be password to open that protected post. 

Yes that opened up the protected post. It was very long but the jist of it was the creds for ftp login. The username is nickburns and the password is supposed to be super ez to guess.

So i used same username as the password and it worked.

__ftp target_ip 65534__

It gave me a readme file with dir name to web server. It didn't work on port 80 so we try on port 8008.

It takes us to the website but we can't see anything. But it says:
```
Nick's sup3r s3cr3t dr0pb0x - only me and Steve Jobs can see this content
```
We can make it seem like we are looking at the website from an iphone using burp-suite and changing the user-agent.

Under Proxy > Options > Match and Replace, there's a way to match the User-Agent and Replace with a regex emulating iOS.

Now we can just refresh the page and we get access to the contents. But now it says we need to get the name of sub-website ending with .html extension.

we can use gobuster and rockyou.txt for this. Running that for sometime we get that the website was fallon1.html

__gobuster dir -u target-ip -w /usr/share/wordlists/rockyou.txt -a (user-angent/IOS) -x .html__

user-agent can be copied from burpsuite. 

In the meantime, we can enumerate more on the WordPress site. I use wpscan to collect a list of users:

__wpscan --url target_ip/prehistoricforest -e__

We get 4 usernames we can try dictionary attack on any of them.

__wpscan --url target_ip/prehistoricforest --wordlist usr/share/wordlists/rockyou.txt --username tom__

We get the creds here ___tom:tomtom1___.

And we get the third flag, a hint and the proctected zip file. 

__wget --user-agent=AGENT url__

Downloading all of them on our system. We read the hint. It's for the directory to crack the password of the zip file.

__crunch 13 13 -t bev,%%@@^1995 -o dic.txt__.

__fcrackzip -u -D -p dic.txt -v t0msp4ssw0rdz.zip__

The password turned out to be: ___bevH00tr$1995___

opening the passwords.txt file we see 4 passwords but the one about _Callahan Auto Server_ is interesting because of it's footnote.

Last half of the ssh creds of this user are on that site. 

___bigtommysenior:fatguyinalittlecoat1938!!___

We login to port 22 using these creds and get the 4th flag. It also gave me the path to where our 5th flag is.

It was hidden in the / directory. But it can be only accessed by user www-data. So we have to get a reverse shell into the server.

In the password protected post we saw:
```
The Callahan Auto Web site is usually pretty stable.  But if for some reason the page is ever down, you guys will probably go out of business.  But, thanks to *me* there’s a backup called callahanbak.bak that you can just rename to index.html and everything will be good again.
```

We need to restore the Callahan Web Page by copying over callahanbak.bak to index.html located in /var/www/html.

Following the path: __var/thatsg0nnaleaveamark/NickIzL33t/P4TCH_4D4MS__.

We see a upload.php file which only uploads jpeg files. We can rename our reverse-shell file .jpeg and upload it. Then we can rename it in the server shell we have open here.

For all this uploading file and navigating we have run burpsuite again and have the user-agent as IOS/iphone.

Then we just navigate over our reverse shell file while listening on the port mentioned in the reverse-shell.php file.

There now we have the 5th flag. Now we just have combine all the flags and form a master password to open the LOOt.zip in bigtommysenoir /home dir.

___master password: B34rcl4wsZ4l1nskyTinyHeadEditButtonButtcrack___

DONE!

```
YOU CAME.
YOU SAW.
YOU PWNED.

Thanks to you, Tommy and the crew at Callahan Auto will make 5.3 cajillion dollars this year.

GREAT WORK!
```
