from pwn import *

p = process("./times-up")

expr = p.readline()[10:-1]
p.sendline(str(eval(expr)))

print(p.recvall())
