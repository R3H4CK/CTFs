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
