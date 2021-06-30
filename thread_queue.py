#!/usr/bin/env python



import threading
import Queue
import time



class WorkerThread(threading.Thread) :
	def __init__(self, queue) :
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self) :
		print "IN WorkerThread"
		while True :
			counter = self.queue.get()
			print "Ordered to sleep for %d"%counter
			time.sleep(counter)
			print "Finished Sleeping for %d seconds"%counter
			self.queue.task_done()


queue = Queue.Queue()

for i in range(10) :
	print "Creating WorkerThread: %d"%i
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "Woeker Thread created %d !!!"%i


for j in range (10) :
	queue.put(j)


queue.join()


print "ALL TASK ARE OVER !!!!"
