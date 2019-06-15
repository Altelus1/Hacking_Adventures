

def pkcs7_padding(message, block_size):

	pad_value = block_size - (len(message)%block_size)
	return message + (chr(pad_value))*pad_value
	

