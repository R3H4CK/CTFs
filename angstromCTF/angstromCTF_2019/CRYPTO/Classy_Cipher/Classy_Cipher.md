# Classy Cipher
<blockquote>
20 points, 789 solves  
Every CTF starts off with a Caesar cipher, but we're more classy.  
  
Author: defund
</blockquote>

## Summary
* ASCII shift cipher
* classical cipher

## Analysis
``` python
text = "d]Wc7H:oW5YgUFS7]D\9fGS^iGHSUF9bHSg9WIf9q"

print(len(text))

cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for ch in text:
    if ch.islower():
        cnt1 += 1
    elif ch.isupper():
        cnt2 += 1
    elif ch.isdigit():
        cnt3 += 1
    else:
        cnt4 += 1
print(cnt1, cnt2, cnt3, cnt4, sep='\n')

for ch in text:
    if not ch.isalpha() and not ch.isdigit() and ch != ' ':
        text = text.replace(ch, '')
for word in text.split(' '):
    if word in text:
        print(word)
```

## Solve
``` python
text = ":<M?TLH8<A:KFBG@V"

def encrypt(plain, key):
    plain = list(plain)
    for i in range(len(plain)):
        plain[i] = chr((ord(plain[i]) + key) % 128)
    return ''.join(plain)

def decrypt(cipher, key):
    cipher = list(cipher)
    for i in range(len(cipher)):
        cipher[i] = (ord(cipher[i]) - key) % 128
        if cipher[i] < 0:
            cipher[i] += 128
        cipher[i] = chr(cipher[i])
    return ''.join(cipher)


for key in range(1, 128):
    print("%03d: %s" % (key, decrypt(text, key)))
```
문제에서 시저 암호를 언급했고 우리는 더 Classy하다고 했다. 암호문에 알파벳과 숫자 이외에 다른 문자가 포함되어 있는 것으로 보아 ASCII 시프트 암호(ASCII shift cipher)이다.  

flag: `actf{so_charming}`
