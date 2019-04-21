import socket
import random

def generate_key():
	
	fir_key = ""
	
	for i in range(6):
		f_digit = random.randint(0,9)
		s_digit = random.randint(0,9)
		
		while (f_digit ^ s_digit ^ 0x42) >= ord('F'):
			s_digit = (s_digit + 1) % 10
			
		fir_key += (str(f_digit)+str(s_digit))
		
	keys = 	["48","84","59","95"]
	sec_key = ""
	
	for i in range(6):
		sec_key += keys[random.randint(0,3)]
	
	return fir_key+sec_key
	

HOST = "keygen.tghack.no"
PORT = 2222

gen_keys = []

while True:
	
	key = generate_key()
	
	if key not in gen_keys:
		gen_keys.append(key)

	if len(gen_keys) >= 250:
		break

clsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clsock.connect((HOST, PORT))

msg = clsock.recv(1024).decode('latin-1')
print(msg)

count = int(msg.split(" ")[1].split("/")[0])
while count <= 250:
	
	print(str(count)+" - sending: "+gen_keys[count-1])
	clsock.send((gen_keys[count-1]+'\n').encode('latin-1'))
	
	msg = clsock.recv(1024).decode('latin-1')
	if "{" in msg:
		print(msg)
		break

	count = int(msg.split("\n")[1].split(" ")[1].split("/")[0])

clsock.close()










