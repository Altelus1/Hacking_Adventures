def score_ecb(ciphertext):
	
	LENGTH = len(ciphertext)
	
	blocks = [ciphertext[i:i+16] for i in range(0,len(ciphertext)-1,16)]
	
	score = 0
	for i in range(len(blocks)):
		for j in range(i+1, len(blocks)):
			if blocks[i] == blocks[j]:
				score += 1

	return score


filename = "8.txt"
contents = ""


with open(filename, "r") as rf:
	contents = rf.read()

contents = contents.split("\n")

scores = []

for i in range(len(contents)):
	
	#ciphertext = base64.b64decode(contents[i])
	ciphertext = bytes.fromhex(contents[i])
	scores.append([i,score_ecb(ciphertext)])	

for item in scores:
	print(item)









