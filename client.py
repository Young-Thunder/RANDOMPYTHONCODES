#!/usr/bin/python

import socket
import sys

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.connect((sys.argv[1], 8000))


while 1 :
	userInput = raw_input("Please Enter a String:")
	tcpSocket.send(userInput)
	print tcpSocket.recv(2048)


tcpSocket.close()

