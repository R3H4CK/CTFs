from pwn import *

p = process("./times-up")

chall = p.recv()
chall = chall[len('Challenge: '):chall.index('\n')]

p.sendline(str(eval(chall)))

print(p.recvall())
