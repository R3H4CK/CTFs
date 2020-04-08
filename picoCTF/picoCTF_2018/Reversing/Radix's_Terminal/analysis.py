import sys

alphabet = "ABCDEFGHIZKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
mod = [2, 1, 0]

def check_password(s):
    v18 = len(s)
    n = 4 * ((v18 + 2) / 3)
    v20 = 4 * ((v18 + 2) / 3)
    v1 = [None for i in range(16 * ((4 * ((v18 + 2) / 3) + 16) / 0x10))]
    s1 = [None for i in range(n)]
    v15, v16 = 0, 0
    while v15 < v18:
        if v15 >= v18:
            v3 = 0
        else:
            v15 += 1
            v2 = v15
            v3 = ord(s[v2])
        v22 = v3
        if v15 >= v18:
            v5 = 0
        else:
            v15 += 1
            v4 = v15
            v5 = ord(s[v4])
        v23 = v5;
        if v15 >= v18:
            v7 = 0
        else:
            v15 += 1
            v6 = v15;
            v7 = ord(s[v6])
        v24 = v7
        v25 = (v23 << 8) + (v22 << 16) + v7
        v16 += 1
        v8 = v16
        s1[v8] = alphabet[(v25 >> 18) & 0x3F]
        v16 += 1
        v9 = v16
        s1[v9] = alphabet[(v25 >> 12) & 0x3F]
        v16 += 1
        v10 = v16
        s1[v10] = alphabet[(v25 >> 6) & 0x3F]
        v16 += 1
        v11 = v16
        s1[v11] = alphabet[v25 & 0x3F]
    for i in range(mod[v18 % 3]):
        s1[n - 1 - i] = 61
    try:
        s1 = s1.remove(None)
    except ValueError:
        pass
    for i in range(len(s1)):
        s1[i] = chr(s1[i])
    s1 = ''.join(s1)
    return s1[:n] == "cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfMjk1ODA5OTN9"[:n]

if len(sys.argv) > 1:
    if check_password(sys.argv[1]):
        print("Incorrect Password!")
    else:
        print("Congrats, now where's my flag?")
else:
    print("Please provide a password!")
