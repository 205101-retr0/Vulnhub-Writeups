first the nmap scan shows there is only one port 80
ctrl + u comments we get a hidden dir.

using dirb and common.txt dict we find that there is a dir called /log 
going to /log we find another hidden dir /DaigonAlley and a password : OjppbGlrZXNvY2tz

pass : OjppbGlrZXNvY2tz(base64) == ilikesocks(ascii)

we find in /Diagonalley something like this: +++++ +++++ [->++ +++++ +++<] >.<++ +[->+ ++<]> ++.<+ ++[-> —<] >—-
..<++ ++[-> ++++< ]>+++ ++++. <++++ [->– –<]> .<+++ [->++ +<]>+ .<+++ +[->- —<] >–.< ++++[ ->+++ +<]>+ +++.- -.<++ +[->- –<]> —– .<+++ [->++ +<]>+ +++.< 
this is brainfuck language translates to donn.

running dirb on url/DiagonAlley we get wp login page as one of the results.

Gudging by the machine name and stuff we can guess the username being draco 
or we can use wpscan to enumerate the users.

login creds to wp-admin were user = draco and password = slytherin(password is his house).


now things get a little complicated.
 
kali has php reverse shell to find it we use 'locate'.

we change the ip to local and listen on our own deamon that we set up.

i want it to trigger when the page throws an E404 so we can edit the theme. and add our reverse shell code to the end of 404.php and save changes

now we goto our terminal and setup a listener and trigger a E404.

we got a shell now spawn a ttyl and export TERM=xterm.

we are logged in as www-data lets change that to dobby we have the password.

and there we have our first flag but cat doesnt work on a spawned shell do lets use more.

Now we try to root acess using the setuid find (find / -perm -u=s -type f 2>/dev/null)(google for more info).

we kno that there is a setuid usr/bin/find we can now goto GTFObin and find the priv esc code

(./find . -exec /bin/sh -p \; -quit)

goto /usr/bin first and then exec this line.

and there it is we have root access goto to root folder and read proof.txt.

So the brainfuck lang thing was useless.




