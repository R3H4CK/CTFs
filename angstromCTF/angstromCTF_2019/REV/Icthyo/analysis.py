from ctypes import *
import sys
from PIL import Image

libc = CDLL("libc.so.6")

rows = []

def read_file(fp):
    im = Image.open(fp)
    # PIL is impossible to check depth.
    if im.format != 'PNG':
        print("%s must be PNG" % fp)
        exit(1) 
    if im.size != (256, 256):
        print("%s must be 256 x 256" % fp)
        exit(1)
    if im.mode != 'RGB':
        print("%s must be RGB" % fp)
        exit(1)
    global rows
    rows = list(map(list, im.getdata()))

def encode():
    try:
        msg = input("message (less than 256 bytes): ")
        if len(msg) > 256:
            raise Exception("The input size is must be less or equal then 256.")
    except Exception as e:
        print("Exception:", e)
    msg = list(map(ord, msg))
    for i in range(len(msg), 256):
        msg.append(ord('\000'))
    global rows
    for i in range(256):
        for j in range(256):
            rows[j][0] ^= libc.rand() & 1
            rows[j][1] ^= libc.rand() & 1
            rows[j][2] ^= libc.rand() & 1
        for k in range(0, 256, 32):
            msg_bit = (msg[i] >> k // 32) & 1
            if rows[k][2] & 1:
                rows[k][2] ^= 1
            rows[k][2] |= (rows[k][0] ^ rows[k][1]) & 1 ^ msg_bit

def write_file(fp):
    im = Image.new('RGB', (256, 256))
    global rows
    rows = map(tuple, rows)
    im.putdata(list(rows))
    im.save(fp)


if len(sys.argv) != 3:
    print("USAGE: %s in.png out.png")
    exit(1)
libc.srand(libc.time(None))
read_file(sys.argv[1])
encode()
write_file(sys.argv[2])
