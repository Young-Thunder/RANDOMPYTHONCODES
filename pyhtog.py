#!/usr/bin/python

import os

for item in os.listdir("/") :
	if os.path.isfile(item) :
		print item + "IS A FILE"
	elif os.path.isdir(item) :
		print item + "IS A DIRECTORY"


	else:
		print "unknown!"


