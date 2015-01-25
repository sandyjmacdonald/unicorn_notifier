#!/usr/bin/env python

import skywriter
import signal
import os
from socket import *

host = '192.168.0.XX'
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

@skywriter.tap(repeat_rate=2)
def tap_detected(location):
	if location == 'center':
		UDPSock.sendto('tap', addr)

signal.pause()
UDPSock.close()
os._exit(0)
