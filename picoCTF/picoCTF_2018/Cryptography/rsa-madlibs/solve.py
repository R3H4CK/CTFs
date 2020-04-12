from pwn import *

def xgcd(a, b):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while b:
        q, r = a // b, a % b
        s = s0 - q * s1
        t = t0 - q * t1
        a, b = b, r
        s0, s1 = s1, s
        t0, t1 = t1, t
    return (a, s0, t0)

sh = remote("2018shell.picoctf.com", 50652)

data = sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):").split('\n')
q = int(data[-5].split(' : ')[1])
p = int(data[-4].split(' : ')[1])
n = p * q
sh.sendline("y")
sh.sendlineafter("n: ", str(n))

data = sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):").split('\n')
p = int(data[-5].split(' : ')[1])
n = int(data[-4].split(' : ')[1])
q = n // p
sh.sendline("y")
sh.sendlineafter("q: ", str(q))

sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
sh.sendline("n")

data = sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):").split('\n')
q = int(data[-5].split(' : ')[1])
p = int(data[-4].split(' : ')[1])
totient = (p - 1) * (q - 1)
sh.sendline("y")
sh.sendlineafter("totient(n): ", str(totient))

data = data = sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):").split('\n')
M = int(data[-6].split(' : ')[1])
e = int(data[-5].split(' : ')[1])
n = int(data[-4].split(' : ')[1])
C = pow(M, e, n)
sh.sendline("y")
sh.sendlineafter("ciphertext: ", str(C))
sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
sh.sendline("n")

data = sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):").split('\n')
q = int(data[-6].split(' : ')[1])
p = int(data[-5].split(' : ')[1])
e = int(data[-4].split(' : ')[1])
totient = (p - 1) * (q - 1)
d = xgcd(e, totient)[1]
if d < 0:
    d += totient
sh.sendline("y")
sh.sendlineafter("d: ", str(d))

data = sh.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):").split('\n')
C = int(data[-6].split(' : ')[1])
p = int(data[-7].split(' : ')[1])
n = int(data[-4].split(' : ')[1])
q = n // p
totient = (p - 1) * (q - 1)
e = int(data[-5].split(' : ')[1])
d = xgcd(e, totient)[1]
if d < 0:
    d += totient
M = pow(C, d, n)
sh.sendline("y")
sh.sendlineafter("plaintext: ", str(M))

data = sh.recv()
print(data)

if "YAHHH! That one was a great madlib!!!" in data:
    print(unhex(hex(M)[2:]))

sh.interactive()
