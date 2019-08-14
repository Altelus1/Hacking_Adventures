import struct

choice = int(input("""
	Input choices:
	[1] - Money
	[2] - All Command Lists
"""))

filename = "..\\1647 - Zoids - Legacy (U)(Venom).sav"

with open(filename, "rb") as rf:

	contents = rf.read()

out = b""
new_checksum = b""
CHECKSUM_ADDR = 0x6b43

if choice == 1:

	MONEY_ADDRESS = 0x6b3f
	MONEY_BYTE_LENGTH = 4

	current_money = contents[MONEY_ADDRESS:MONEY_ADDRESS+4]
	current_checksum = bytes([contents[CHECKSUM_ADDR]]) + b'\x00'
	current_checksum = struct.unpack("<H", current_checksum)[0]
	print(current_checksum)

	print("[*] Current money : {}".format(struct.unpack("<I",current_money)[0]))
	print("[*] Current checksum : {}".format(hex(current_checksum)))

	new_val = int(input("[?] New money value: "))
	new_val = struct.pack("<I",new_val)
  
	new_checksum = current_checksum

	for i in range(MONEY_BYTE_LENGTH):
		new_checksum -= (new_val[i] - contents[MONEY_ADDRESS + i])
		new_checksum %= 256

	out = contents[:MONEY_ADDRESS] + new_val + bytes([new_checksum]) + contents[CHECKSUM_ADDR+1:]


elif choice == 2:

	COMMAND_LIST_ADDR = 0x6b37
	COMMAND_LIST_BYTE_LENGTH = 6 # 6 * 
	current_checksum = bytes([contents[CHECKSUM_ADDR]]) + b'\x00'
	current_checksum = struct.unpack("<H", current_checksum)[0]

	all_commands = b'\xff'*6
	new_checksum = current_checksum

	for i in range(COMMAND_LIST_BYTE_LENGTH):
		new_checksum -= (all_commands[i] - contents[COMMAND_LIST_ADDR+i])
		new_checksum %= 256

  out = contents[:COMMAND_LIST_ADDR] + all_commands + contents[COMMAND_LIST_ADDR+COMMAND_LIST_BYTE_LENGTH:]
	out = out[:CHECKSUM_ADDR] + bytes([new_checksum]) + out[CHECKSUM_ADDR+1:]

print("[*] New checksum : {}".format(new_checksum))
print("[*] Length of output : {}".format(len(out)))

with open(filename, "wb") as wf:
	wf.write(out)

print("[*] Changes Made! Try opening the game again!")
