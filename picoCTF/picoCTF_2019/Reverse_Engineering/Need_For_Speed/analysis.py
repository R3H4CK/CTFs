import signal

flag = [0x32, 0x75, 0x21, 0x73, 0x20, 0x68, 0x22, 0x47, 0x23, 0x53, 0xa, 0x58, 0x46, 0x56, 0x9, 0x5e, 0x47, 0x57, 0xd, 0x59, 0x18, 0x55, 0x7, 0x5b, 0x4a, 0x5e, 0x1f, 0x4f, 0x4b, 0x1f, 0x5f, 0xc, 0x58, 0x8, 0x9, 0xe, 0x57, 0x9, 0x4e, 0x4f, 0x1f, 0x59, 0x15, 0x58, 0x19, 0x52, 0x16, 0x1c, 0x13, 0x50, 0x1d, 0x52, 0x14, 0x1d, 0x9]
key = 0

def decrypt_flag(key):
    i = 0
    while True:
        if i > 54:
            break
        flag[i] ^= key >> (i % 2) * 8 & 0xff
        if i % 3 == 2:
            key += 1
        i += 1

def calculate_key():
    i = -1145669436
    i -= 1
    while i != -572834718:
        i -= 1
    return 3722132578

def alarm_handler():
    print("Not fast enough. BOOM!")
    exit(0)

def set_timer():
    if signal.signal(signal.SIGALRM, alarm_handler) == -1:
        print("\n"
              "\n"
              "Something bad happened here. \n"
              "If running on the shell server\n"
              "Please contact the admins with \"need-for-speed.c:%d\".\n")
        exit(0)
    signal.alarm(1)

def get_key():
    print("Creating key...")
    global key 
    key = calculate_key()
    print("Finished")

def print_flag():
    print("Printing flag:")
    decrypt_flag(key)
    print(''.join(map(chr, flag)))

def header():
    print("Keep this thing over 50 mph!")
    for i in range(27):
        print(chr(61), end='')
    print()


header()
set_timer()
get_key()
print_flag()
