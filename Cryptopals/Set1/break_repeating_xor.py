import base64

def get_hamming_distance(str1, str2):
	bits = ""
	
	for i in range(len(str1)):
		bits += bin(ord(str1[i]) ^ ord(str2[i]))[2:].zfill(8)

	return bits.count("1")
	
