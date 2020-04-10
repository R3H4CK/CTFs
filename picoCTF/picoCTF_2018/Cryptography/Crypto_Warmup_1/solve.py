text = "llkjmlmpadkkc"
key = "thisisalilkey"

def encrypt(plain, key):
    plain = list(plain)
    j = 0
    for i in range(len(plain)):
        j %= len(key)
        if plain[i].islower():
            if key[j].islower():
                plain[i] = (ord(plain[i]) - 97 + ord(key[j]) - 97) % 26
            elif key[j].isupper():
                plain[i] = (ord(plain[i]) - 97 + ord(key[j]) - 65) % 26
            plain[i] += 97
        elif plain[i].isupper():
            if key[j].islower():
                plain[i] = (ord(plain[i]) - 65 + ord(key[j]) - 97) % 26
            elif key[j].isupper():
                plain[i] = (ord(plain[i]) - 65 + ord(key[j]) - 65) % 26
            plain[i] += 65
        else:
            plain[i] = ord(plain[i])
        j += 1
    return ''.join(map(chr, plain))

def decrypt(cipher, key):
    cipher = list(cipher)
    j = 0
    for i in range(len(cipher)):
        j %= len(key)
        if cipher[i].islower():
            if key[j].islower():
                cipher[i] = (ord(cipher[i]) - ord(key[j])) % 26
            elif key[j].isupper():
                cipher[i] = (ord(cipher[i]) - 97 - ord(key[j]) + 65) % 26
            if cipher[i] < 0:
                cipher[i] += 26
            cipher[i] += 97
        elif cipher[i].isupper():
            if key[j].islower():
                cipher[i] = (ord(cipher[i]) - 65 - ord(key[j]) + 97) % 26
            elif key[j].isupper():
                cipher[i] = (ord(cipher[i]) - ord(key[j])) % 26
            if cipher[i] < 0:
                cipher[i] += 26
            cipher[i] += 65
        else:
            cipher[i] = ord(cipher[i])
        j += 1
    return ''.join(map(chr, cipher))

print(decrypt(text, key))
