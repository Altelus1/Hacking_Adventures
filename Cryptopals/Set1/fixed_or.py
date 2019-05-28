def xor_bytes(str1, str2):
	raw_hex1 = bytes.fromhex(str1)
	raw_hex2 = bytes.fromhex(str2)

	result = []	

	for i in range(len(raw_hex2)):
		result.append(hex(raw_hex1[i] ^ raw_hex2[i])[2:]) 
	return "".join(result)

x = "1c0111001f010100061a024b53535009181c"
y = "686974207468652062756c6c277320657965"

print(xor_bytes(x,y))
