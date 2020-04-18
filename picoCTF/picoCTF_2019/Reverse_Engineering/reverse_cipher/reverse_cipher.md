# reverse_cipher
> We have recovered a binary and a text file. Can you reverse the flag. Its also found in /problems/reverse-cipher_5_6e21330f568439d366f5c038e32e5572 on the shell server.

## Summary
* file I/O
* reverse

## Analysis
``` python
try:
    f1 = open("flag", "r")
except FileNotFoundError:
    print("No flag found, please make sure this is run on the server")
try:
    f2 = open("rev_this", "a")
except:
    print("please run this on the server")

flag = f1.read(24)
if len(flag) <= 0:
    exit(0)

for i in range(8):
    f2.write(flag[i])
for i in range(8, 23):
    ch = ord(flag[i])
    if i & 1:
        ch -= 2
    else:
        ch += 5
    f2.write(chr(ch))
f2.write(flag[i + 1])
f2.close()
f1.close()
```

## Solve
``` python
with open("rev_this", "r") as f:
    data = f.read()

with open("flag", "a") as f:
    f.write(data[:8])
    for i in range(8, 23):
        if i & 1:
            ch = chr(ord(data[i]) + 2)
        else:
            ch = chr(ord(data[i]) - 5)
        f.write(ch)
    f.write(data[i + 1])
```
인덱스를 검사해서 최하위 비트가 존재하면 +2 아니면 -5를 더하는데 이를 그대로 역산 해주면 된다.  

flag: `picoCTF{r3v3rs3321bda1b}`
