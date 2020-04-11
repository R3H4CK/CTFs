text = "d]Wc7H:oW5YgUFS7]D\9fGS^iGHSUF9bHSg9WIf9q"

def encrypt(plain, key):
    plain = list(plain)
    for i in range(len(plain)):
        plain[i] = chr((ord(plain[i]) + key) % 128)
    return ''.join(plain)

def decrypt(cipher, key):
    cipher = list(cipher)
    for i in range(len(cipher)):
        cipher[i] = ord(cipher[i]) - key % 128
        if cipher[i] < 0:
            cipher[i] += 128
        cipher[i] = chr(cipher[i])
    return ''.join(cipher)

for i in range(1, 128):
    print("%03d: %s" % (i, decrypt(text, i)))
