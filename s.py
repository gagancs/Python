#! /usr/bin/python2

import socket,time
#	ipv4 / ipv6		UDP SGTREAM
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
	msg=raw_input("enter your data: ")
	s.sendto(msg,("127.0.0.1", 8888))
	time.sleep(1)
	print x.recvfrom(100)
