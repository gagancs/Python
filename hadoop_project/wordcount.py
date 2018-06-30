#!/usr/bin/python3

import os
import cgi,cgib

print("content-type:text/html")
print ("")

web_data=cgi.FieldStorage()
location =web_data.getvalue('x')
#out =web_data.getvalue('y')
#os.system("hadoop jar /usr/share/hadoop/hadoop-expamples-1.2.1.jar wordcount "+location+" >>/output/wordcount")
print(location)

