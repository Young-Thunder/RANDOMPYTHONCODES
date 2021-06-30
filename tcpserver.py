#! /usr/bin/env python


import SocketServer



class EchoHandler(SocketServer.BaseRequestHandler) :

	def handle(self) :

		print "GOT A CONNECTION FROM :", self.client_address

	   	data = 'dummy'

		while len(data) :

		 	data = self.request.recv(1024)
			print"CLient sent:" + data
			self.request.send(data)

			print "CLIENT LEFT"



serverAddr  = ("0.0.0.0",9000)

server = SocketServer.TCPServer(serverAddr, EchoHandler)

server.serve_forever()


