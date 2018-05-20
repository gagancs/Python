#! /usr/bin/python2

import socket
import time

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("127.0.0.1",8300))

while True:
	data = s.recvfrom(1000)
	time.sleep(1)
	print "the messege is : ", data[0]
	print "the IP is : ", data[1][0]
	msg=raw_input("Enter your messege")
	s.sendto(msg,data[1])
