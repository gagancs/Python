#!/usr/bin/python2

import sys
#picking up the source and destination file from cmd
files=sys.argv[1:3]

#extracting the source file
src_file=files[0]

#extracting the destination file
dst_file=files[1]

#opening source file
f1=open(src_file,"r")
data=f1.read()
f1.close()

#opening second file
f2=open(dst_file,"w")
#copying data from file 1 to file2
f2.write(data)
f2.close()

print "copying "+src_file+" to "+dst_file+"...!!"
