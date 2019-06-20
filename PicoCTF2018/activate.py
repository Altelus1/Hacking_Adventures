from itertools import permutations
"""
0x39 >= x > 0x2f


0x5a >= x > 0x40 
"""

def get_serial_val(serial):
	
	total = 0
	print(serial)
	
	for i in range(len(serial)-1):
		#print(serial[i])
		if ord(serial[i]) > 0x40:
			total += ((ord(serial[i]) - 0x37) + 1) * (i+1)
		elif ord(serial[i]) > 0x2f:
			total += ((ord(serial[i]) - 0x30) + 1) * (i+1)
#print(total)
			
	print(total%0x24)
	return total

def is_valid(serial):
	
	stat_val = 0x38e38e39	
	total = get_serial_val(serial)
	
	res = (total * stat_val) & 0xffffffff
	
	res_shr = (res >> 3) & 0xff
	res_shl = (res_shr << 3) & 0xff
	
	tot_res = (((res_shr + res_shl ) & 0xffffffff) << 2 & 0xffffffff)
	
	total -= tot_res
	
	last_char = ord(serial[len(serial)-1])
	
	if last_char > 0x40:
		last_char -= (last_char - 0x37)
	elif last_char > 0x3f:
		last_char -= (last_char - 0x30)
		
	print(bin(last_char)[2:].zfill(32))
	print(bin(total)[2:].zfill(32))
	
	return last_char == tot_res
	

s = '01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'	
x = 'T10101Z103010102'

print(is_valid(x))
#print(is_valid(x[::-1]))
#x = '0123450123450123456'
#perms = [''.join(p) for p in permutations(x)]

#print('Starting bruteforcing')

#for perm in perms:
#	if is_valid(perms):
#		print(perm)
#		break
		
		
		
		

	