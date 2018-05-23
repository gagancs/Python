#! /usr/bin/python2

t=raw_input("enter tuple elements")

print t

s=raw_input("enter the string you want to search")

n=len(s)
for i in t:
	k=0
	for j in range (0,n-1):
		if(s[j]==i[j])
			k=k+1
print k

