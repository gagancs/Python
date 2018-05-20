#! /usr/bin/python2

import socket
#	ipv4 / ipv6		UDP SGTREAM
x=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind
x.bind(("127.0.0.1",8888))

#recieve 


while True:
	#print x.recivefrom(1000)
	data=x.recvfrom(1000)
	print "data from client :",data[0]
	#print "IP of client: ",data[1][0]
	reply=raw_input("plz type your reply: ")
	x.sendto(reply,data[1][0])
