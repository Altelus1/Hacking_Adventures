from xeger import Xeger
import aes_cbc_decryptor as ACD
import aes_cbc_encryptor as ACE
import random
import base64
import math


filename = '/home/jethromagbanua/Downloads/text_set'
with open(filename, 'rb') as rb:
	contents = rb.read()


ENCRYPTION_COUNT = 100
x = Xeger(limit=16)
encrypted_messages = []

for i in range(ENCRYPTION_COUNT):
	message = ''
	try:
		start = random.randint(0, int(math.floor(len(contents)-401)))
		message = contents[start:400+(start)+random.randint(0,100)]
		print(start)
	except Exception as e:
		print("Boundary exceeded...trying again")
		i -= 1
		continue
	key = x.xeger("[a-zA-Z0-9]{16}")
	
	encrypted = ACE.encrypt_cbc(message,key)

	encrypted_messages.append([encrypted, key])


with open('encrypted_texts.txt', 'w') as wf:
	for item in encrypted_messages:
		print("{}\nkey: {}\n\n".format(item[0],item[1]))





