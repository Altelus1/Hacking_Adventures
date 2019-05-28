def decode_xor(cipher, key):
	cipher_byte = bytes.fromhex(cipher)
	key_byte = bytes.fromhex(key)

	result = []
	
	for i in range(len(cipher_byte)):
		result.append(chr(cipher_byte[i] ^ key_byte[0]))

	return "".join(result)

cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

for i in range(256):
	print(str(i)+" - "+decode_xor(cipher, hex(i)[2:].zfill(2)))

#message = "Cooking MC's like a pound of bacon at byte 88"
