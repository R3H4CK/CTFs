from z3 import *

X = IntVector('x', 16)
s = Solver()

for i in range(16):
    s.add(X[i] >= 0, X[i] <= 35)

s.add((X[0] + X[1]) % 36 == 14)
s.add((X[2] + X[3]) % 36 == 24)
s.add((X[2] - X[0]) % 36 == 6)
s.add((X[3] + X[1] + X[5]) % 36 == 4)
s.add((X[4] + X[2] + X[6]) % 36 == 13)
s.add((X[4] + X[3] + X[5]) % 36 == 22)
s.add((X[8] + X[6] + X[10]) % 36 == 31)
s.add((X[4] + X[1] + X[7]) % 36 == 7)
s.add((X[12] + X[9] + X[15]) % 36 == 20)
s.add((X[14] + X[13] + X[15]) % 36 == 12)
s.add((X[9] + X[8] + X[10]) % 36 == 27)
s.add((X[12] + X[7] + X[13]) % 36 == 23)

print(s.check())
print(s.model())
