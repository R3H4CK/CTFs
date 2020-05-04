def encrypt(plain):
    plain = list(plain)
    for i in range(len(plain)):
        if plain[i].islower():
            plain[i] = chr((ord(plain[i]) - ord('a') + 13) % 26 + ord('a'))
        elif plain[i].isupper():
            plain[i] = chr((ord(plain[i]) - ord('A') + 13) % 26 + ord('A'))
    return ''.join(plain)

def decrypt(cipher):
    cipher = list(cipher)
    for i in range(len(cipher)):
        if cipher[i].islower():
            cipher[i] = chr((ord(cipher[i]) - ord('a') + 13) % 26 + ord('a'))
        elif cipher[i].isupper():
            cipher[i] = chr((ord(cipher[i]) - ord('A') + 13) % 26 + ord('A'))
    return ''.join(cipher)


text = "Rotate by 13"

print(encrypt(encrypt(text))) # ROT 13 is encrypt == decrypt
