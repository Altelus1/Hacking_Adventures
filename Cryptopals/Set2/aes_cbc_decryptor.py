from Crypto.Cipher import AES
import pkcs7_pad as p7p
import math
import base64

def decrypt(aes_obj, ciphertext):
    plaintext = aes_obj.decrypt(ciphertext)
    return plaintext

def chop_blocks(string_stream, block_size):
    no_blocks = int(math.ceil(len(string_stream)/block_size))
    return [string_stream[i*block_size:(i+1)*block_size] for i in range(no_blocks)]

def xor_two_blocks(block1, block2, block_size):
    xored_block = b''
    
    for i in range(block_size):	
        xored_block += (block1[i] ^ block2[i]).to_bytes(1, byteorder="big", signed=False)

    return xored_block

def decrypt_cbc(encrypted_message, key, IV = b'\x00'*16, block_size=16):
    aes_obj = AES.new(key, AES.MODE_ECB)
    cipher_blocks = chop_blocks(encrypted_message, block_size)
    cipher_blocks.insert(0, IV)

    plain_blocks = []

    for i in range(len(cipher_blocks)-1,0,-1):
        plain_block = xor_two_blocks(cipher_blocks[i-1] ,decrypt(aes_obj, cipher_blocks[i]), block_size)
        plain_blocks.insert(0, plain_block.decode('latin-1')) 

    return plain_blocks 














