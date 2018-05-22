#! /usr/bin/python2

import sys,time

print sys.argv[1:]
def add(*x):
	sum1=0
	for i in x:
		sum1=sum1+i
	print sum1
add(1,2,3,4)
