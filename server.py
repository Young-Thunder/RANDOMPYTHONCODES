#!/usr/bin/env python

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0",8000))

tcpSocket.listen(3)

print "Waiting for the client!!!"

(client, (ip, port)) = tcpSocket.accept()

print "Received the connection from :", ip

print "Starting ECHO Output"

data = 'dummy'

while len(data) :

	data = client.recv(2048)
	print "Client sent:",data
	client.send(data)

print "Closing Connection"

client.close()
