#!/usr/bin/python2

import urllib.request, urllib.error, urllib.parse


url = raw_input("Enter the URL: ")

fhand = urllib.request.urlopen('http://'+url)

for line in fhand:
	print " line.strip() "
