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
