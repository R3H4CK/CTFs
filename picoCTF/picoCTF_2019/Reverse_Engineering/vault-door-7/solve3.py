flag = b""
X = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304823, 962880562, 895706419]

for x in X:
    flag += x.to_bytes(4, byteorder="big")
print(flag.decode())
