import aes_cbc_decryptor as ACD
import base64

filename = "decr.txt"
contents = ""
key = "4n7mK1Nu2HFRyMrd"
block_size = 16

with open(filename, "rb") as rb:
    contents = rb.read()

#contents = contents.replace("\n","")
contents = base64.b64decode(contents)

plain_blocks = ACD.decrypt_cbc(contents, key=key)

print(b''.join(plain_blocks),end="")