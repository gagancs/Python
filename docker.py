#!/usr/bin/python3

import os
import time
x=range(10)

for i in x:
	os.system(docker run -itd --name node+"+i+"+ centos6:hadoopv1)
	time.sleep(1)
