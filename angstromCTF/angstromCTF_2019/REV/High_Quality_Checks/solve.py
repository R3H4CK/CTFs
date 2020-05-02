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
