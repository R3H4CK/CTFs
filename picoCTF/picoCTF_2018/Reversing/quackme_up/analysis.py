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
