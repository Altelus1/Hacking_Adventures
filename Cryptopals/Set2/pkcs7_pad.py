def pkcs7_padding(message, block_size):

	#if type(message) == bytes :
	#		message = message.decode('utf-8')
	pad_value = block_size - (len(message)%block_size)
	return (message + (bytes(pad_value))*pad_value)