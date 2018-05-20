#! /usr/bin/python2

import webbrowser
import time
#import beautifulsoup

option='''
Press 1:
Press 2:
Press 3:
Press 4:
Press 5:
Press 6:
Press 7:
'''

print option

ch= raw_input("enter your choice")

if ch=='1':
	s=raw_input("enter your strings ")
	sl=s.strip().split()
	webbrowser.open_new_tab("https://www.google.com/search=?q"+sl)


