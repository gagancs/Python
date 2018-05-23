#! /usr/bin/python2

import webbrowser
import time
#import beautifulsoup

option='''
Press 1: search keywords in different tabs
Press 2: search keyword images in diff tabs
Press 3: extract urls
Press 4: 
Press 5:
Press 6:
Press 7:
'''

print option

ch= raw_input("enter your choice")

if ch=='1':
	s=raw_input("enter your strings ")
	s1=s.strip().split()
	for i in s1
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)


