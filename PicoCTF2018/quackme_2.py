
hex_stream = "11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 20 30 00 45 05 35 40 65 C1"
hex_stream = hex_stream.replace(" ","")
hex_stream = bytes.fromhex(hex_stream)
out = ""

print(hex_stream)
for hex_c in hex_stream:
	#rol8
	temp = hex_c ^ 0x16
	temp = (temp >> 4 | temp << 4) & 0xff
	out += chr(temp)
	
print(out)