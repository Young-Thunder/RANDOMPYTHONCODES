#!/usr/bin/python



import sys

print "Printing all lines with systemd in it"

logfile = open(sys.argv[1])

for line in logfile.readlines() :
	if line.lower().find("systemd") != -1 :

		print line

print "DONE"
