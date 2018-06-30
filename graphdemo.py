#!/usr/bin/python2

import matplotlib.pyplot as pt

x=[10,20]
y=[20,40]

pt.title("Analytics Figure")
pt.xlabel("Time")
pt.ylabel("Speed")
pt.plot(x,y)
pt.scatter(x,y, s=100)
pt.show()
