# Crypto Warmup 1
> Crpyto can often be done by hand, here's a message you got from a friend, llkjmlmpadkkc with the key of thisisalilkey. Can you use this table to solve it?.

## Summary
* vigenere cipher
* classical cipher

## Analysis
``` python
ciphertext = "llkjmlmpadkkc"
key = "thisisalilkey"

# table
for i in range(26):
    for ch in range(ord('A'), ord('Z') + 1):
        print(chr((ch - ord('A') + i) % 26 + ord('A')), end='')
    print()
```

## Solve
``` python
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
        j += 1
    return ''.join(map(chr, cipher))

print(decrypt(text, key))
```
문제의 암호문과 키는 decode.fr의 <a href="https://www.dcode.fr/vigenere-cipher" target="_blank">비즈네르 암호</a>(vigenere cipher)의 예제이다.  

flag: `picoCTF{secretmessage}`
