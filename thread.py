#!/usr/bin/env python


import thread
import time



def worker_thread(id) :
	print "Thread is ID %d now alive "%id

	count = 1
	while True :
		print "Thread Id %d has counter value %d"% (id, count)
		time.sleep(2)
		count +=1



for i in range(5):
	thread.start_new_thread(worker_thread, (i,))


print "MAin thread"


while True :
	pass
