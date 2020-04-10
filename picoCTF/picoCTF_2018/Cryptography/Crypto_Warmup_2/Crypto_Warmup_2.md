# Crypto Warmup 2
> Cryptography doesn't have to be complicated, have you ever heard of something called rot13? cvpbPGS{guvf_vf_pelcgb!}

## Summary
* ROT13
* classical cipher

## Analysis
``` python
text = "cvpbPGS{guvf_vf_pelcgb!}"

print(len(text))
for i in range(len(text)):
    for j in range(len(text)):
        if text[i:j] in text[i+1:]:
            print(text[i:j])
```

## Solve
``` python
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
```

<a href="https://rot13.com/" target="_blank">ROT13</a>으로 암호화되어있는데 회전을 13번 하는 이유는 암호화와 복호화 같은 유일한 횟수이기 때문이다.  

flag: `picoCTF{this_is_crypto!}`
