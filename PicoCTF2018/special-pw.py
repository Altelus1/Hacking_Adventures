
byte_stream = '\x7b\x18\xa6\x36\xda\x3b\x2b\xa6\xfe\xcb\x82\xae\x96\xff\x9f\x46\x8f\x36\xa7\xaf\xfe\x93\x8e\x3f\x46\xa7\xff\x82\xcf\xce\xb3\x97\x17\x1a\xa7\x36\xef\x2b\x8a\xed'

byte_stream = byte_stream.encode('latin-1')

for counter in range(len(byte_stream)-4, -1, -1):
	to_proc = int.from_bytes(byte_stream[counter:counter+4], byteorder="little")
	print(bin(to_proc))
	to_proc = ((to_proc >> 0xb) | (to_proc << (32-0xb))) &0xffffffff
	print(bin(to_proc))
	to_proc = ((((to_proc & 0xffff) << 0x5) | ((to_proc & 0xffff) >> (16-0x5))) &0x0000ffff) | (to_proc & 0xffff0000)
	print(bin(to_proc))
	to_proc = to_proc ^ 0x0000009d
	print(bin(to_proc))
	byte_stream = byte_stream[0:counter]+to_proc.to_bytes(4, byteorder='little')+byte_stream[counter+4:]

print(byte_stream)

'''
From PicoCTF 2018 challenge "special-pw" under Reverse Engineering
'''
