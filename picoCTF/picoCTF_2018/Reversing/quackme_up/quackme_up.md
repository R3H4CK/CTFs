# quackme up
> The duck puns continue. Can you crack, I mean quack this program as well? You can find the program in /problems/quackme-up_2_bf9649c854a2615a35ccdc3660a31602 on the shell server.

## Summary
* Rotate
* XOR

## Analysis
``` c
from pybitrot import rol8, ror8

encryptedBuffer = "11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 35 40 65 95 75 00 30 85 C1"

def print_hex(s, n):
    for i in range(n):
        if i > 0:
            print(" ", end='')
        print("%02X" % s[i], end='')
    print()

def encrypt(s):
    n = len(s)
    for i in range(n):
        s[i] = ror8(rol8(ord(s[i]), 4) ^ 0x16, 8)
    return n

print("We're moving along swimmingly. Is this one too fowl for you?")
s = list(input("Enter text to encrypt: "))
n = encrypt(s)
print("Here's your ciphertext: ", end='')
print_hex(s, n)
print(f"Now quack it! : {encryptedBuffer}")
print("That's all folks.")
```

## Solve
``` python
from pybitrot import rol8, ror8

flag = ""
encryptedBuffer = [0x11, 0x80, 0x20, 0xE0, 0x22, 0x53, 0x72, 0xA1, 0x01, 0x41, 0x55, 0x20, 0xA0, 0xC0, 0x25, 0xE3, 0x35, 0x40, 0x65, 0x95, 0x75, 0x00, 0x30, 0x85, 0xC1]

for enc in encryptedBuffer:
    flag += chr(ror8(rol8(enc, 8) ^ 0x16, 4))
print(flag)
```

회전연산(rotate)과 XOR은 모두 고유한 역원이 존재하는 연산이므로 순서대로 역산을 해주면 된다. 

flag: `picoCTF{qu4ckm3_2e786ab9}`
