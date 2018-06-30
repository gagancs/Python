#!/usr/bin/python2

import requests
from bs4 import BeautifulSoup

data= requests.get("http://static.cricinfo.com/rss/livescores.xml")
text_data=data.text
#print text_data

soup= BeautifulSoup(text_data, "html.parser")
print soup
score_teams=[]

try:
	item_ele= soup.find_all("item")
	for item in item_ele:
		title=item.find_all("title")
		for text_data in title:
			print score_teams.append(text_data.text)
	
except:
	print "No Live match"
'''
for text_data in score_teams:
    if text_data.find('/')>=0:
        print data+'\n'
print '\n\n ********  STARTING SOON  *********\n'
for text_data in score_teams:
    if text_data.find ('/') <0:
        print text_data+'\n'
''' 
