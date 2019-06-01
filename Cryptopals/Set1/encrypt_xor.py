def encrypt_xor(message, key):
	
	cipher = ""
	
	for i in range(len(message)):
		cipher += hex(ord(message[i])^ord(key[i%len(key)]))[2:].zfill(2)
	
	return cipher
		
key = "ICE"
m1 = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
print(encrypt_xor(m1, key))
