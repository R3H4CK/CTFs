flag = ""
table = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC0, 0xB4, 0xD1, 0xD2, 0x85, 0xA4, 0xA5, 0xC1, 0x85]

def switchBits(c, p1, p2):
    mask1 = 1 << p1 & 0xff
    mask2 = 1 << p2 & 0xff
    bit1 = c & mask1 & 0xff
    bit2 = c & mask2 & 0xff
    rest = c & ~(mask1 | mask2) & 0xff
    shift = p2 - p1 & 0xff
    result = ((bit1 << shift) | (bit2 >> shift) | rest) & 0xff
    return result


for sc in table:
    for ch in range(33, 127):
        c = switchBits(ch, 1, 2)
        c = switchBits(c, 0, 3)
        c = switchBits(c, 5, 6)
        c = switchBits(c, 4, 7)
        c = switchBits(c, 0, 1)
        c = switchBits(c, 3, 4)
        c = switchBits(c, 2, 5)
        c = switchBits(c, 6, 7)
        if sc == c:
            flag += chr(ch)
            break
print(flag)
