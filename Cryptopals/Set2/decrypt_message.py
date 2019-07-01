import aes_cbc_decryptor as ACE
import base64

filename = "encrypted.txt"
contents = ""
key = "YELLOW SUBMARINE"
block_size = 16

with open(filename, "r") as rf:
    contents = rf.read()

contents = contents.replace("\n","")
contents = base64.b64decode(contents)

plain_blocks = ACE.decrypt_cbc(contents, key=key)

print(''.join(plain_blocks),end="")
