# Icthyo
<blockquote>
130 points, 88 solves  
Long before stegosaurus roamed the earth, another species prowled the sea; here is an artist's rendition.  
  
Author: defund
</blockquote>

## Summary
* steganography
* bitwise operation

## Analysis
``` python
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
```

## Solve
``` python
from PIL import Image

im = Image.open("out.png")

bin = ""
for i in range(256):
    for j in range(0, 256, 32):
        rgb = im.getpixel((j, i))
        bin += str((rgb[0] ^ rgb[1]) & 1 ^ rgb[2] & 1)

flag = ""
for i in range(len(bin)//8):
    try:
        flag += chr(int(bin[i*8:i*8+8][::-1], base=2))
    except:
        continue
        
print(flag)
```
`Analysis`의 encode 함수를 보면 중첩 반복문의 첫 번째 내측 반복문은 모든 RGB를 의사 난수 비트와 xor 하는데, LSB가 바뀌어도 큰 영향은 없다.  
두 번째 내측 반복문에서 메시지의 비트를 하나씩 가져오고 RGB의 LSB가 존재하면 없앤다 그 다음 B = B | LSB(R ^ G) ^ LSB(msg)를 수행하게 된다.  
즉, 32번째 RGB 마다 LSB(msg)를 하나씩 숨기는 것인데 PIL로 이미지를 읽고 간단한 역산을 해주면 된다.  

flag: `actf{lurking_in_the_depths_of_random_bits}`
