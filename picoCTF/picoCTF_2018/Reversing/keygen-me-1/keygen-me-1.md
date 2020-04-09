#

## Summary
* Keygen

## Analysis
``` python
import sys

def check_valid_char(ch):
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
        v2 = s[v3]
    if v3 == 16:
        return 16
    else:
        return 0

def c_ord(ch):
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
    return v2 % 24 == c_ord(s[v4 - 1]) 

def print_flag():
    try:
        with open("flag.txt", "r") as f:
            flag = f.read(64)
        print(flag)
    except OSError:
        print("Flag File is Missing.")

if len(sys.argv) > 1:
    if check_valid_key(sys.argc[1]):
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
