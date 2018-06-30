#!/usr/bin/python2

import mysql.connector as mysql


print "		Database connection with my registration form"

name=raw_input("Enter your name")
password=raw_input("Enter your password")
ID=raw_input("enter your id")
email=raw_input("Enter your Email")

#Connection with database
conn=mysql.connection(user="root",password="root", host="localhost",database="formdata")

if conn.is_connected():
	print "connection done"
else:
	print "Something is wrong..!!"

#creating cursor instance
cur=conn.cursor()

#query
query='insert into register'
#execution of query
cur.execute()
