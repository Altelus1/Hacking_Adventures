from Crypto.Cipher import AES
import base64

def decrypt(key, ciphertext):
	aes_obj = AES.new(key, AES.MODE_ECB)
	plaintext = aes_obj.decrypt(ciphertext)

	return plaintext


filename = "7.txt"
contents = ""
key = "YELLOW SUBMARINE"

with open(filename,"r") as rf:
	contents = rf.read()

contents = contents.replace("\n","")
contents = base64.b64decode(contents)
print(decrypt(key, contents))
