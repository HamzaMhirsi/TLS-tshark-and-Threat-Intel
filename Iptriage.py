#!/usr/bin/python
import mmap

"""
The Ip is the field reiceved in the frame we will need to scan the external IP 
we will use here the file merged with the code "merge.py"
"""

file = open("reputation.data")
IP ='207.241.231.146'
s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
if s.find(IP) != -1:
	print "This "+IP+" is blacklisted"
file.close()
