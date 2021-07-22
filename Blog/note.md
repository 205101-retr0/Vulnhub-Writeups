machine ip : 10.10.40.170

kwheel - cutiepie1			## wpscan

msfconsole -- goto wp_crop_rce

odd setuid was /usr/sbin/checker -- which checks if ur an admin or not

download that using meterpreter on download command

checker converting it to c code using ghidra we get that admin env variable needs to be anything but a empty string.

so we "export admin=somethinglessOffensive"

and we can run it /usr/sbin/checker and we get root access

after that we can find the user.txt flag using the find command.