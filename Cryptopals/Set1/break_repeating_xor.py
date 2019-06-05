import base64
import detect_single_xor as DSX

def get_hamming_distance(str1, str2):
	bits = ""
	
	for i in range(len(str1)):
		bits += bin(ord(str1[i]) ^ ord(str2[i]))[2:].zfill(8)

	return bits.count("1")

def get_keysize_block(str1, keysize):
	
	ret_blocks = []
	for i in range(0, len(str1), keysize):
		if i + keysize >= len(str1):
			break
		ret_blocks.append(str1[i:i+keysize])
		
	return ret_blocks
	
filename = "to_break_2.txt"

with open(filename, "r") as rf:
	contents = rf.read()
contents = base64.b64decode(contents).decode('latin-1').replace("\n", "")
#print(contents)
hamm_avg = []
navg_threshhold = 3.2
top_navg = []

#for keysize in range(2,int(len(contents)/2)):
for keysize in range(2,41):
	
	keysize_blocks = get_keysize_block(contents, keysize)
	#print(keysize_blocks)
	hamm_distances = 0
	for counter in range(len(keysize_blocks)-1):
		hamm_distances += get_hamming_distance(keysize_blocks[counter],keysize_blocks[counter+1])
	
	hamm_distances = hamm_distances/(len(keysize_blocks)-1)
	hamm_avg.append([keysize, hamm_distances, hamm_distances/keysize, keysize_blocks])
	
print("Keysize\t\tAVG_HAMM\t\t\tNormAVG_HAMM: \nNAVG Threshold: "+str(navg_threshhold)+"\n-----------------------------------------------------------------------")
for item in hamm_avg:
	if item[2] < navg_threshhold:
		top_navg.append(item)
		print("{}\t\t{}\t\t{}".format(
			item[0],
			format(item[1], ".15f"),
			format(item[2],".15f")
		))
		
print("\nAttempting to break....")

scores = []

for i in range(len(top_navg)):
	byte_blocks = ['' for j in range(len(top_navg[i][3][0]))]
	#print(len(byte_blocks))
	for j in range(len(byte_blocks)):
		byte_blocks[j] += ''.join([item[j] for item in top_navg[i][3]])
	
	#print(byte_blocks)
	
	prob_key = ""
	nbyte_decrypted = []
	for item in byte_blocks:
		selected = '\x00'
		selected_decoded = ""
		score = 0
		for j in range(32, 123):
			decoded = DSX.decode_xor(item.encode('latin-1'), hex(j)[2:].zfill(2))
			curr_score = DSX.score_it(decoded)
			if curr_score > score:
				selected = chr(j)
				score = curr_score
				selected_decoded = decoded
		nbyte_decrypted.append(selected_decoded)
		prob_key += selected
	
	scores.append(["key : "+prob_key, nbyte_decrypted])
	
for item in scores:
	decrypted = ""
	for i in range(len(item[1][0])):
		decrypted += ''.join([byte_decrypted[i] for byte_decrypted in item[1]])
	
	print(item[0]+"\nmessage : "+decrypted)

"""
NEED SOME TWEAKING
STILL NEED TO INVESTIGATE TO MAKE THIS SCRIPT MORE ACCURATE
(well it's *NOT* already accurate to begin with lol
"""
