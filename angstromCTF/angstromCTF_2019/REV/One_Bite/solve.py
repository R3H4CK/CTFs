flag = ""
table = "]_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA"

for ch in table:
    flag += chr(ord(ch) ^ 0x3C)
print(flag)
