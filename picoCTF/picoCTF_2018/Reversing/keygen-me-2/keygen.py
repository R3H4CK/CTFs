key = ""
X = [14, 0, 20, 4, 18, 0, 11, 25, 0, 7, 20, 0, 32, 2, 29, 17]

for i in range(16):
    if X[i] > 10:
        key += chr(X[i] + 55)
    else:
        key += chr(X[i] + 48)
print(key)
