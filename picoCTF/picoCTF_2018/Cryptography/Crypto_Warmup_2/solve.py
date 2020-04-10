text = "cvpbPGS{guvf_vf_pelcgb!}"

def encrypt(plain):
    plain = list(plain)
    for i in range(len(plain)):
        if plain[i].islower():
            plain[i] = (ord(plain[i]) - 97 + 13) % 26 + 97
        elif plain[i].isupper():
            plain[i] = (ord(plain[i]) - 65 + 13) % 26 + 65
        else:
            plain[i] = ord(plain[i])
    return ''.join(map(chr, plain))

def decrypt(cipher):
    cipher = list(cipher)
    for i in range(len(cipher)):
        if cipher[i].islower():
            cipher[i] = (ord(cipher[i]) - 97 + 13) % 26 + 97
        elif cipher[i].isupper():
            cipher[i] = (ord(cipher[i]) - 65 + 13) % 26 + 65
        else:
            cipher[i] = ord(cipher[i])
    return ''.join(map(chr, cipher))

print(encrypt(text)) # ROT13 is enc == dec
