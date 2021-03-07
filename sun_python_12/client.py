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

# ваш ip, ваш порт
host = socket.gethostbyname(socket.gethostname())
port = 0

# сервер ip, сервер порт
server = ("192.168.1.132", 11719)

# создает сокет
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

name = input("$ name: ")
# отправляет сообщение на сервер
s.sendto(("["+name+"] => join chat ").encode("utf-8"), server)
time.sleep(0.2)

# собирает сообщения с сервера
rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

# закрывает соединение (для безопасности)
rT.join()
s.close()
