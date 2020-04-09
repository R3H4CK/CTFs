import sys

table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def c_ord(ch):
    ch = ord(ch)
    if ch > 47 and ch <= 57:
        return ch - 48
    if ch <= 64 or ch > 90:
        print("Found Invalid Character!")
        sys.exit(0)
    return ch - 55

def validate_key(s):
    v4 = len(s)
    v2 = 0
    for i in range(v4 - 1):
        v2 += (c_ord(s[i]) + 1) * (i + 1)
    return v2 % 0x24 == c_ord(s[v4 - 1])

for ch1 in table:
    for ch2 in table:
        for ch3 in table:
            key = ch1*8 + ch2 + ch3*7
            if validate_key(key):
                print(key)
