import socket
import telnetlib


HOST = 'p1.tjctf.org'
PORT = 8009

clsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clsock.connect((HOST, PORT))

msg = clsock.recv(1024).decode('latin-1')

clsock.send('sycamore\n'.encode('latin-1'))
msg = clsock.recv(1024).decode('latin-1')

while "step" in msg:
	if "{" in msg or "'one'" in msg:
		print("FLAG: {}".format(msg))
		break
	print(msg, end="")
	to_send = msg.split("'")[1]
	print(" "+(to_send))
	clsock.send((to_send+"\n").encode('latin-1'))
	msg = clsock.recv(1024).decode('latin-1')
	
t = telnetlib.Telnet()
t.sock = clsock
t.interact()

clsock.close()
