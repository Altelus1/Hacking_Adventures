#
#import stuff here
#

filename = "10_plain.txt"
contents = ""
key = "YELLOW SUBMARINE"
block_size = 16

with open(filename, "r") as rf:
    contents = rf.read()

contents = contents.encode('latin-1')
aes_obj = AES.new(key, AES.MODE_ECB)
plain_blocks = chop_blocks(contents, block_size)
#print(plain_blocks)

encrypted = encrypt_cbc(plain_blocks)


print(encrypted.decode('latin-1'))
