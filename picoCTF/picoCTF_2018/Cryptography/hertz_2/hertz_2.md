# hertz 2
> This flag has been encrypted with some kind of cipher, can you decrypt it? Connect with nc 2018shell.picoctf.com 39961.

## Summary
* monoalphabetic substitution cipher
* classical cipher

## Analysis
``` python
text = "Yif wonhr axqkp vqu godbc qefx yif tmzj lqs. N hmp'y aftnfef yinc nc cohi mp fmcj bxqatfd np Bnhq. Ny'c mtdqcy mc nv N cqtefl m bxqatfd mtxfmlj! Qrmj, vnpf. Ifxf'c yif vtms: bnhqHYV{coacynyoynqp_hnbifxc_mxf_yqq_fmcj_lpsmqkdejf}"

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
flag = ""
text = "Yif wonhr axqkp vqu godbc qefx yif tmzj lqs. N hmp'y aftnfef yinc nc cohi mp fmcj bxqatfd np Bnhq. Ny'c mtdqcy mc nv N cqtefl m bxqatfd mtxfmlj! Qrmj, vnpf. Ifxf'c yif vtms: bnhqHYV{coacynyoynqp_hnbifxc_mxf_yqq_fmcj_lpsmqkdejf}"
table = "mahlfvsingrtdpqbwxcyoekujzMAHLFVSINGRTDPQBWXCYOEKUJZ"

for ch in text:
    for i in range(len(table)):
        if ch == table[i]:
            if table[i].islower():
                flag += chr(97 + i)
            elif table[i].isupper():
                flag += chr(39 + i)
    if not ch.isalpha():
        flag += ch
print(flag)
```
이 문제도 <a href="https://www.guballa.de/substitution-solver" target="_blank">모노 알파베틱 치환 암호</a>(mono alphabetic substitution cipher)를 사용한다. 링크의 break cipher 기능을 사용하면 쉽게 해독할 수 있다.  

flag: `picoCTF{substitution_ciphers_are_too_easy_dngaowmvye}`
