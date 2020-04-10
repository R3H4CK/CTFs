# caesar cipher 1
> This is one of the older ciphers in the books, can you decrypt the message? You can find the ciphertext in /problems/caesar-cipher-1_1_6fbf7a9ce0aac23bab1c37836cc20c3b on the shell server.

## Summary
* ROT14
* classical cipher

## Analysis
``` python
text = "vgefmsaapaxpomqemdoubtqdxoaxypeo"

print(len(text))
for i in range(len(text)):
    for j in range(len(text)):
        if text[i:j] in text[i+1:]:
            print(text[i:j])
```

## Solve
``` python
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
```
오리지널 시저 암호(caesar cipher)는 키가 3이다. 해당 암호문은 ROT14로 복호화 할 수 있다.  
시저 암호(카이사르 암호)는 줄리어스 시저(가이우스 율리우스 카이사르(라틴어: Gaius Iulius Caesar))의 이름을 딴 것이다.

flag: `picoCTF{justagoodoldcaesarcipherlcolmdsc}`
