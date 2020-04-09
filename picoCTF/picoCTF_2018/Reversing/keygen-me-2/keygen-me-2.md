# keygen-me-2
> The software has been updated. Can you find us a new product key for the program in /problems/keygen-me-2_2_5374d282dd09441ebd3055cb968eefff

## Summary
* keygen
* simultaneous equation
* Z3 Probing

## Analysis
``` python 
import sys

def check_valid_char(ch):
    ch = ord(ch)
    return ch > 47 and ch <= 57 or ch > 64 and ch <= 90

def c_ord(ch):
    ch = ord(ch)
    if ch > 47 and ch <= 57:
        return ch - 48
    if ch <= 64 and ch > 90:
        print("Found Invalid Character!")
        sys.exit(0)
    return ch - 55

def check_valid_key(s):
    if not id(s):
        return 0
    v2 = s[0]
    v3 = 0
    while ord(v2):
        if check_valid_char(v2):
            return 0
        v3 += 1
        try: 
            v2 = s[v3]
        except IndexError:
            pass
        if v3 == 16:
            return 16
        else:
            return 0

def mod(a, m):
    if a % m >= 0:
        return a % m
    else:
        return a % m + m

def key_constraint_01(s):
    return mod(c_ord(a[0]) + c_ord(a[1]), 36) == 14

def key_constraint_02(s):
    return mod(c_ord(s[2]) + c_ord(s[3]), 36) == 24

def key_constraint_03(s):
    return mod(c_ord(s[2]) - c_ord(s[0]), 36) == 6

def key_constraint_04(s):
    return mod(c_ord(s[3]) + c_ord(s[1]) + c_ord(s[5]), 36) == 4

def key_constraint_05(s):
    return mod(c_ord(s[4]) + c_ord(s[2]) + c_ord(s[6]), 36) == 13

def key_constraint_06(s):
    return mod(c_ord(s[4]) + c_ord(s[3]) + c_ord(s[5]), 36) == 22

def key_constraint_07(s):
    return mod(c_ord(s[8]) + c_ord(s[6]) + c_ord(s[10]), 36) == 31

def key_constraint_08(s):
    return mod(c_ord(s[4]) + c_ord(s[1]) + c_ord(s[7]), 36) == 7

def key_constraint_09(s):
    return mod(c_ord(s[12]) + c_ord(s[9]) + c_ord(s[15]), 36) == 20

def key_constraint_10(s):
    return mod(c_ord(s[14]) + c_ord(s[13]) + c_ord(s[15]), 36) == 12

def key_constraint_11(s):
    return mod(c_ord(s[9]) + c_ord(s[8]) + c_ord(s[10]), 36) == 27

def key_constraint_12(s):
    return mod(c_ord(s[12]) + c_ord(s[7]) + c_ord(s[13]), 36) == 23

def validate_key(s):
    len(s)
    return key_constraint_01(s) \
        and key_constraint_02(s) \
        and key_constraint_03(s) \
        and key_constraint_04(s) \
        and key_constraint_05(s) \
        and key_constraint_06(s) \
        and key_constraint_07(s) \
        and key_constraint_08(s) \
        and key_constraint_09(s) \
        and key_constraint_10(s) \
        and key_constraint_11(s) \
        and key_constraint_12(s)

def print_flag():
    try:
        with open("flag.txt", "r") as f:
            flag = f.read(64)
            print(flag, end='')
    except OSError:
        print("Flag File is Missing.")

if len(sys.argv) > 1:
    if check_valid_key(sys.argv[1]):
        if validate_key(sys.argv[1]):
            print("Product Activated Successfully: ", end='')
            print_flag();
        else:
            print("INVALID Product Key.")
    else:
        print("Please Provide a VALID 16 byte Product Key.")
else:
    print("Usage: ./activate <PRODUCT_KEY>")
```

## Solve
``` python
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
```

``` python
key = ""
X = [14, 0, 20, 4, 18, 0, 11, 25, 0, 7, 20, 0, 32, 2, 29, 17]

for i in range(16):
    if X[i] > 10:
        key += chr(X[i] + 55)
    else:
        key += chr(X[i] + 48)
print(key)
```
변수와 조건이 굉장히 많이 보이는데 이 문제의 의도는 Z3를 사용한 연립방정식의 해를 구하는 것이다.  
연립방정식의 해를 구한 후 다시 char로 되돌리고 서버 shell의 해당 파일의 인자로 넣으면 된다.  

flag: `picoCTF{c0n5tr41nt_50lv1nG_15_W4y_f45t3r_2923966318}`
