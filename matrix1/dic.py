#!/usr/bin/python3

import string

def func():
	ch = string.ascii_lowercase + string.ascii_uppercase + string.digits
	for i in ch:
		for j in ch:
			s = "k1ll0r"
			s = s + str(i) + str(j);
			print(s)

if __name__ == "__main__":
	func()
