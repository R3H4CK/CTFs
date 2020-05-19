# Half and Half
<blockquote>
50 points, 383 solves  
Mm, coffee. Best served with half and half!  
  
Author: defund
</blockquote>

## Summary
* xor
* classical cipher

## Solution
``` python
shake = '\x15\x02\x07\x12\x1e\x100\x01\t\n\x01"'
print(len(shake))

flag = ""
i = 0
for sip in shake:
    tmp = ord(sip) ^ ord('actf{'[i%5])
    if tmp >= 33 and tmp <= 126:
        flag += chr(tmp)
    else:
        flag += '?'
    i += 1
print(flag) # actf{???????taste??????}

flag = ""
for sip in shake:
    flag += chr(ord(sip) ^ ord('_'))
print(flag) # actf{??????_taste??????}

flag = ""
i = 0
for sip in shake:
    flag += chr(ord(sip) ^ ord('coffee'[i%5]))
    i += 1
print(flag) # actf{coffee_tastes_good}
```
flag를 반으로 나누어 xor 하는 암호이므로 포함하는 문자열을 찾아서 xor하고 이를 통해 찾은 문자열을 다시 활용하는 방식으로 풀면 된다.

flag: `actf{coffee_tastes_good}`
