flag = ['\000' for i in range(32)]
x = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304823, 962880562, 895706419]

for i in range(len(x)):
    for j in range(4):
        flag[i * 4 + 3 - j] = chr(x[i] >> j * 8 & 0xff)
print(''.join(flag))
