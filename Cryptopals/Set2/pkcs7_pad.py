

def pkcs7_padding(message, block_size):

	pad_value = block_size - len(message)
	return message + (chr(pad_value))*pad_value
	

