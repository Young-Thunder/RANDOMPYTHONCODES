#!/usr/bin/env python



import os

def child_process() :
	print "I AM THE CHILD PROCESS AND MY PID IS %d" %os.getpid()
	print "The child is exiting"


def parent_process() :

	print "I am the parent process with PID : %d"%os.getpid()
	childpid = os.fork()

	if childpid == 0 :
		#we are inside the child
		child_process()
	else:
		#we are the insder the parent 

		print"we our inside the parent process"
		print"OUR CHILD PID IS :%d"%childpid
	while True:
		pass

parent_process()
