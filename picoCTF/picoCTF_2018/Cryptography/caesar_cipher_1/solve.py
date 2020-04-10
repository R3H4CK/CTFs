text = "vgefmsaapaxpomqemdoubtqdxoaxypeo"

def encrypt(plain, key):
    plain = list(plain)
    for i in range(len(plain)):
        if plain[i].islower():
            plain[i] = (ord(plain[i]) - 97 + key) % 26 + 97
        elif plain[i].isupper():
            plain[i] = (ord(plain[i]) - 65 + key) % 26 + 65
        else:
            plain[i] = ord(plain[i])
    return ''.join(map(chr, plain))

def decrypt(cipher, key):
    cipher = list(cipher)
    for i in range(len(cipher)):
        if cipher[i].islower():
            cipher[i] = (ord(cipher[i]) - 97 - key) % 26
            if cipher[i] < 0:
                cipher[i] += 26
            cipher[i] += 97
        elif cipher[i].isupper():
            cipher[i] = (ord(cipher[i]) - 65 - key) % 26
            if cipher[i] < 0:
                cipher[i] += 26
            cipher[i] += 65
        else:
            cipher[i] = ord(cipher[i])
    return ''.join(map(chr, cipher))

for key in range(1, 26):
    print("%2d: " % key + "picoCTF{"+encrypt(text, key)+"}")
