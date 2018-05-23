#!/usr/bin/pyhton2

import time as t

def ok():
	while True:
		print "this is okay"
		t.sleep(1)
		google() #calling second function recursively

def google():
	while True:
		print "Yo google"
		t.sleep(2)
		ok()

ok() #starting of recursive calling
