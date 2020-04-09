import sys

def check_valid_char(ch):
    ch = ord(ch)
    return ch > 47 and ch <= 57 or ch > 64 and ch <= 90

def c_ord(ch):
    ch = ord(ch)
    if ch > 47 and ch <= 57:
        return ch - 48
    if ch <= 64 or ch > 90:
        print("Found Invalid Character!")
        sys.exit(0)
    return ch - 55

def check_valid_key(s):
    if not id(s[0]):
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

def mod(a, m):
    return a % m if a % m >= 0 else a % m + m

def key_constraint_01(s):
    return mod(c_ord(s[0]) + c_ord(s[1]), 36) == 14

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
