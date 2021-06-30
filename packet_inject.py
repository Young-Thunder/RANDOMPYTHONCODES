#!/usr/bin/env python

import socket
import struct




rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("ens33", socket.htons(0x0800)))

packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')

# 6bit 6 bits 2 bits destionation address, soucre mac addres eth0 header

rawSocket.send(packet + "Hello THERE")
