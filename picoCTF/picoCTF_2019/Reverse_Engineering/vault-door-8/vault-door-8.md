# vault-door-8
> Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: VaultDoor8.java

## Summary
* Brute Force
* Inverse Function

## Analysis
``` python
class VaultDoor8:
    def scramble(self, password):
        a = bytearray(password, 'utf-8')
        for b in range(len(a)):
            c = a[b]
            c = self.switchBits(c, 1, 2)
            c = self.switchBits(c, 0, 3)
            c = self.switchBits(c, 5, 6)
            c = self.switchBits(c, 4, 7)
            c = self.switchBits(c, 0, 1)
            c = self.switchBits(c, 3, 4)
            c = self.switchBits(c, 2, 5)
            c = self.switchBits(c, 6, 7)
            a[b] = c
        return a

    def switchBits(self, c, p1, p2):
        mask1 = 1 << p1 & 0xff
        mask2 = 1 << p2 & 0xff
        bit1 = c & mask1 & 0xff
        bit2 = c & mask2 & 0xff
        rest = c & ~(mask1 | mask2) & 0xff
        shift = p2 - p1 & 0xff
        result = ((bit1 << shift) | (bit2 >> shift) | rest) & 0xff
        return result

    def checkPassword(self, password):
        scrambled = self.scramble(password)
        expected = bytearray([0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC0, 0xB4, 0xD1, 0xD2, 0x85, 0xA4, 0xA5, 0xC1, 0x85])
        return scrambled == expected


a = VaultDoor8()
f = input("Enter vault password: ")
if a.checkPassword(f):
    print("Access granted.")
else:
    print("Access denied!")
```

# Solve
``` python
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
```
switchBits 함수를 이용하여 비트들을 섞는다. 이 루틴을 그대로 가져와서 브루트포스하면 flag를 구할 수 있다.
``` python
table = bytearray([0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC0, 0xB4, 0xD1, 0xD2, 0x85, 0xA4, 0xA5, 0xC1, 0x85])

def switchBits(c, p1, p2):
    mask1 = 1 << p1 & 0xff
    mask2 = 1 << p2 & 0xff
    bit1 = c & mask1 & 0xff
    bit2 = c & mask2 & 0xff
    rest = c & ~(mask1 | mask2) & 0xff
    shift = p2 - p1 & 0xff
    result = ((bit1 << shift) | (bit2 >> shift) | rest) & 0xff
    return result

def unscramble(password):
    a = password
    for b in range(len(a)):
        c = a[b]
        c = switchBits(c, 6, 7)
        c = switchBits(c, 2, 5)
        c = switchBits(c, 3, 4)
        c = switchBits(c, 0, 1)
        c = switchBits(c, 4, 7)
        c = switchBits(c, 5, 6)
        c = switchBits(c, 0, 3)
        c = switchBits(c, 1, 2)
        a[b] = c
    return a


print(unscramble(table).decode())
```
브루트포스가 아니면 위와같이 역함수(inverse function)를 구해도 된다.  

flag: `picoCTF{s0m3_m0r3_b1t_sh1fTiNg_0c59dbf4d}`
