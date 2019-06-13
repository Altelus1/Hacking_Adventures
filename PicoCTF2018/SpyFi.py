import socket

def chop_to_32(hex_stream):
	return [hex_stream[i*32:(i+1)*32] for i in range(int(len(hex_stream)/32)-1)]

def is_duplicate(hex_lists):
	
	return len(list(set(hex_lists))) < len(hex_lists)

tosend_msg = 'c00l3$t_6081670'
#tosend_msg = '. My situation '

HOST = "2018shell.picoctf.com"
PORT = 33893

agent_code = ""
padding = "01234567890"
padding2 = 'a'*11

while True:
	for i in range(32, 127):
		#i = 93
		clsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clsock.connect((HOST,PORT))	

		msg = clsock.recv(1024)
		msg = clsock.recv(1024)

		send_msg = (padding+tosend_msg+chr(i)+padding2+'\n').encode('latin-1')
		print(send_msg)
		clsock.send(send_msg)

		msg = clsock.recv(1024).decode('latin-1')
		hex_lists = chop_to_32(msg)

		if is_duplicate(hex_lists):
			agent_code += chr(i)
			#padding = padding[0:-1]
			padding2 = padding2[0:-1]
			tosend_msg = tosend_msg[1:] + agent_code[-1]
			break

		clsock.close()
	
	if agent_code[len(agent_code)-1] == ".":
		break
		
	#tosend_msg = tosend_msg[1:] + agent_code[len(agent_code)-1]

print(agent_code)
#picoCTF{@g3nt6_1$_th3_c00l3$t_6081670}