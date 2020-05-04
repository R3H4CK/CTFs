flag = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

for i in range(len(flag)):
    flag[i] = chr(flag[i] + 65 - 1)
flag.insert(7, '{')
flag.append('}')
print(''.join(flag))
