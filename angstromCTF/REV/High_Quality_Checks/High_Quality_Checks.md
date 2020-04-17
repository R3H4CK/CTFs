# High Quality Checks
> After two break-ins to his shell server, kmh got super paranoid about a third! He's so paranoid that he abandoned the traditional password storage method and came up with this monstrosity! I reckon he used the flag as the password, can you find it?  
Author: Aplet123

## Summary
* angr
* troublesome

## Analysis
``` python
def d(ch):
    return ord(ch) == 808531811

def n(num):
    return (num >> 1)

def v(ch):
    return (ord(ch) ^ 0x37) == n(172)

def o(ch):
    ch = ord(ch)
    if ch > 96:
        result = ch - 87
    else:
        result = ch - 48
    return (65537 * (result + (ch << 8)))

def u(ch1, ch2):
    return ord(ch1) == n(220) and o(ch2) == 889533701

def k(ch):
    return o(ch) != 1712285199

def w(s):
    return (ord(s[1]) << 8) + (ord(s[2]) << 16) + ord(s[0]) == 6714467

def e(i):
    return i % 4 / 2

def b(s, i):
    return ord(s[i]) == n(246) + 2 * e(i)

def z(s, j):
    v5, v6 = 0, 0
    for i in range(8):
        v7 = ((1 << i) & j) >> i
        if i & 1:
            v5 += v7 << i / 2
        else:
            v6 += v7 << i / 2
    if ord(s[v5 + 1]) == 117:
        if ord(s[v5 + 1]) == n(220):
            if ord(s[v6]) == n(234) and s[v6 + 1] == 110:
                return 1
    return 0

def s(s):
    v2 = 0
    for i in range(19):
        if o(s[i]) == 1596940079:
            v2 += i + 1
    return v2 == 9

def check(s):
    return d(s[12]) \
        and v(s[0]) \
        and u(s[16], s[17]) \
        and not k(s[5]) \
        and not k(s[9]) \
        and w(s[1]) \
        and b(s, 18) \
        and b(s, 4) \
        and z(s, 108) \
        and s(s)
        

print("Enter your input:")
s = input()

if len(s) > 0x12:
    if check(s):
        print("You found the flag!")
    else:
        print("That's not the flag.")
else:
    print("Flag is too short.")
```

## Solve
``` python
flag = [None for i in range(19)]

def n(num):
    return (num >> 1)

def o(ch):
    ch = ord(ch)
    if ch > 96:
        return (65537 * (ch - 87 + (ch << 8)))
    else:
        return (65537 * (ch - 48 + (ch << 8)))

def e(i):
    return i % 4 // 2

def w():
    for i in range(33, 127):
        for j in range(33, 127):
            for k in range(33, 127):
                if j * 256 + k * 65536 + i == 6714467:
                    return (i, j, k)

def z():
    v5, v6 = 0, 0
    for i in range(8):
        v7 = ((1 << i) & 108) >> i
        if i & 1:
            v5 += v7 << i // 2
        else:
            v6 += v7 << i // 2
    return (v5, v6)


flag[12] = chr(0x63)
flag[13] = chr(0x37)
flag[14] = chr(0x31)
flag[15] = chr(0x30)
flag[0] = chr(n(172) ^ 0x37)
flag[16] = chr(n(220))
flag[17] = chr((889533701 + 87 * 65537) // (257 * 65537))
flag[5] = chr((1712285199 + 87 * 65537) // (257 * 65537))
flag[9] = chr((1712285199 + 87 * 65537) // (257 * 65537))
flag[1], flag[2], flag[3] = map(chr, w())
flag[18] = chr(n(246) + 2 * e(18))
flag[4] = chr(n(246) + 2 * e(4))
v5, v6 = z()
flag[v5] = chr(117)
flag[v5 + 1] = chr(n(220))
flag[v6] = chr(n(234))
flag[v6 + 1] = chr(110)

for i in range(19):
    if flag[i] == None:
        flag[i] = chr((1596940079 + 87 * 65537) // (257 * 65537))
        
print(''.join(flag))
```
각각의 역함수(inverse function)를 구하고 적절히 브루트포스하면 flag를 구할 수 있다.

flag `actf{fun_func710n5}`
