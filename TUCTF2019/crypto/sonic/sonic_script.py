from pwn import *
import enchant


def rot(shift, word):

	ret_str = ""
	
	for item in word:
		ret_str += chr(((ord(item) - 65 + shift) % 26) + 65)

	return ret_str

d = enchant.Dict("en_US")

def check_rot_word(rot_word):
	for i in range(26):

		decr = rot(i,rot_word)
		print(decr)
		if d.check(decr):
			return decr

def recvall(conn):
	msg = b''
	while True:
		try:
			new_block = conn.recv(timeout=1)
			if new_block == b'':
				break
			msg += new_block	
		except EOFError as e:
			break
	return msg



HOST = "chal.tuctf.com"
PORT = 30100

conn = remote(HOST, PORT)

msg = recvall(conn)
word = msg.split("\n")[-2].split(": ")[1]

print("word : {}".format(word))

conn.sendline(check_rot_word(word))

msg = recvall(conn)
print(msg)

conn.close()


















