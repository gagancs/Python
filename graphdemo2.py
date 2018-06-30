#!/usr/bin/python2

import matplotlib.pyplot as pit

x=[10,20]
y=[20,40]

pit.title("Analytics Figure")
pit.xlabel("Time")
pit.ylabel("Speed")
pit.plot(x,y, label = "The Graph 1")
pit.scatter(x,y, s=100, c='r', label="Scatter")
pit.bar(x,y,label="Bar graph")
pit.pie(x,labels=['A','B'], autopct='%1.1f',shadow=True)
pit.legend()
pit.show()
