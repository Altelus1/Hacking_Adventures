import base64
import aes_cbc_encryptor as ACE

filename = "decrypted.txt" #this is also 10_plain.txt
contents = ""
key = "YELLOW SUBMARINE"
block_size = 16

with open(filename, "r") as rf:
    contents = rf.read()

contents = contents.encode('latin-1')

encrypted = ACE.encrypt_cbc(contents, key)

print(encrypted.decode('latin-1'))
