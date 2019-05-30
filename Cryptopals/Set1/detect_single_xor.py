
def score_it(string):

	score = 0
	
	for char in string:
		if ord(char) == 32:
			score += 1
		elif (ord(char) >=65 and ord(char) <=90) or (ord(char) >= 97 and ord(char) <= 122):
			score += 2
		elif ord(char) < 32 or ord(char) > 122:
			score -= 3
		
	return score
    
def decode_xor(cipher, key):
	cipher_byte = bytes.fromhex(cipher)
	key_byte = bytes.fromhex(key)

	result = []
	
	for i in range(len(cipher_byte)):
		result.append(chr(cipher_byte[i] ^ key_byte[0]))

	return "".join(result)

filename = "file.txt"
contents = ""

with open(filename, "r") as rf:
	contents = rf.read()
	
contents = contents.split("\n")
ordering = []
#print(contents)

for i in range(len(contents)):
	for j in range(256):
		decoded = decode_xor(contents[i],hex(j)[2:].zfill(2))
		score = score_it(decoded)
		if score > 40: #tweak this (the score 40) 
			ordering.append([decoded, ""+str(i)+":"+str(j), score])
			
for item in ordering:
	print(item)
		
"""
['Now that the party is jumping\n', '170:53', 50]
The hex string on 170 xored with character '5' (dec value is 53) with a score of 50 
"""
