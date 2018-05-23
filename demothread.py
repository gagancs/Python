#!/usr/bin/python2

import time as t
import thread as th

def ok():
	while True:
		print "this is okay"
		t.sleep(1)
		
def google():
	while True:
		print "Yo google"
		t.sleep(2)

th.start_new_thread(ok,())
th.start_new_thread(google,())

while True:
	pass
