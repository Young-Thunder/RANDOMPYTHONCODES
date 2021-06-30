#!/usr/bin/env python


import signal

def ctrlc_handler(signal, frm) :

	print "HAHA YOU cant kill me !"

print "INSTALLING SIGNAL HANDLER......"
signal.signal(signal.SIGINT, ctrlc_handler)


print "DONE!"


while True :
	pass
