# -*- coding: utf-8 -*-

import socket
import threading
import time
import colorama
import tqdm

def receving (name, sock, switch):
	while not switch:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				print('\n'+data.decode("utf-8"))
                time.sleep(0.2)	
		except:
			pass


# выкл, подключен
shutdown = False
join = False


