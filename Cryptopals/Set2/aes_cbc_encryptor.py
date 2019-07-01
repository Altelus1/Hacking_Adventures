from Crypto.Cipher import AES
import pkcs7_pad as p7p
import math
import base64

def encrypt(aes_obj, message):
    
    ciphertext = aes_obj.encrypt(message)
    return ciphertext

def chop_blocks(string_stream, block_size):
    no_blocks = int(math.ceil(len(string_stream)/block_size))
    return [string_stream[i*block_size:(i+1)*block_size] for i in range(no_blocks)]

def xor_two_blocks(block1, block2, block_size):
    xored_block = b''
    
    for i in range(block_size): 
        xored_block += (block1[i] ^ block2[i]).to_bytes(1, byteorder="big", signed=False)

    return xored_block

def encrypt_cbc(plain_message, key, IV = b'\x00'*16, block_size=16):
    plain_blocks = chop_blocks(plain_message, block_size)

    aes_obj = AES.new(key, AES.MODE_ECB)

    plbl_length = len(plain_blocks)
    plain_blocks[plbl_length-1] = p7p.pkcs7_padding(plain_blocks[plbl_length-1], block_size)
    cipher_blocks = []
    cipher_block = IV

    for plain_block in plain_blocks:
        cipher_block = encrypt(aes_obj, xor_two_blocks(plain_block, cipher_block, block_size))
        cipher_blocks.append(cipher_block.decode('latin-1'))

    ciphertext = None
    ciphertext=''.join(cipher_blocks).encode('latin-1')
    ciphertext = base64.b64encode(ciphertext)

    return ciphertext









