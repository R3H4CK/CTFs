# keygen-me-1
> Can you generate a valid product key for the validation program in /problems/keygen-me-1_0_2b06ee615c1b7021f1eff5829aae5006

## Summary
* Keygen
* Simple compare

## Analysis
``` python
import sys

def check_valid_char(ch):
    ch = ord(ch)
    return ch > 47 and ch <= 57 or ch > 64 and ch <= 90

def check_valid_key(s):
    if not id(s):
        return 0
    v2 = s[0]
    v3 = 0
    while ord(v2):
        if not check_valid_char(v2):
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

def print_flag():
    try:
        with open("flag.txt", "r") as f:
            flag = f.read(64)
        print(flag)
    except OSError:
        print("Flag File is Missing.")

if len(sys.argv) > 1:
    print("6")
    if check_valid_key(sys.argv[1]):
        print("7")
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
```
소스를 Hex-Rays해서 validate_key의 루틴을 Python 코드로 옮기고 적당히 브루트포스를 하는 코드를 작성하면 된다.
``` bash
./activate "999999990UUUUUUU"
```
Product Activated Successfully: picoCTF{k3yg3n5_4r3_s0_s1mp13_2243075891}  

flag: `picoCTF{k3yg3n5_4r3_s0_s1mp13_2243075891}`
