#!/usr/bin/python3

import os
import cgi

print("content-type:text/html")
print ("")

web_data=cgi.FieldStorage()
location =web_data.getvalue('x')
type =web_data.getvalue('y')

if type=='wc':
	#os.system("docker exec node0 hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount "+location+" /output/wordcount.txt")
	os.system("cal")
	print(location)
else:
	os.system("docker exec node0 hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar aggregatewordcount "+location+" /output/wordcount.txt")

#aprint(os.systemI("docker exec node0 hadoop fs -cat /output/wordcount.txt"))

