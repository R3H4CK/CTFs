# caesar cipher 2
> Can you help us decrypt this message? We believe it is a form of a caesar cipher. You can find the ciphertext in /problems/caesar-cipher-2_4_23c82ed24f4436e96acc1f9f22dc8799 on the shell server.

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
```
문장에 알파벳이나 숫자 이외의 문자가 포함되어 있고 시저 암호의 변형이라고 하는 것을 보면 ASCII 시프트 암호(ASCII shift cipher)인 것 같다.  

flag: `picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}`
