#! /usr/bin/python2


#importing BeautifulSoup from bs4
from bs4 import BeautifulSoup
#print dir(BeautifulSoup)

import requests

#getting url from user
url = raw_input("enter the URL you want to search")
r = requests.get("http://"+url)
data=r.text
#print data

soup= BeautifulSoup(data)

print soup

for link in soup.find_all('a'):
	print link.get("href")


