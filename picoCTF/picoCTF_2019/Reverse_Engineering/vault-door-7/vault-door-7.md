# vault-door-7
> This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java

## Summary
* shift
* simple encryption

## Analysis
``` python
class VaultDoor7:
    def passwordToIntArray(self, password):
        x = [0 for i in range(8)]
        hexBytes = bytearray(map(ord, password))
        for i in range(8):
            x[i] = hexBytes[i*4] << 24 \
                | hexBytes[i*4+1] << 16 \
                | hexBytes[i*4+2] << 8 \
                | hexBytes[i*4+3]
        return x

    def checkPassword(self, password):
        if len(password) != 32:
            return False
        x = self.passwordToIntArray(password)
        print(x)
        return x[0] == 1096770097 \
            and x[1] == 1952395366 \
            and x[2] == 1600270708 \
            and x[3] == 1601398833 \
            and x[4] == 1716808014 \
            and x[5] == 1734304823 \
            and x[6] == 962880562 \
            and x[7] == 895706419


vaultDoor = VaultDoor7()
userInput = input("Enter vault password: ")
if vaultDoor.checkPassword(userInput):
    print("Access granted.")
else:
    print("Access denied!")
```

## Solve
``` python
flag = ['\000' for i in range(32)]
x = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304823, 962880562, 895706419]

for i in range(len(x)):
    for j in range(4):
        flag[i * 4 + 3 - j] = chr(x[i] >> j * 8 & 0xff)
print(''.join(flag))
```
입력받은 값을 16진수로 배열로 바꾸고 shift를 이용한 전치로 32비트 패킹을 한다. (solve1.py를 참고)
``` c
#include <stdio.h>

int main(void)
{
	char flag[33] = "\0";
	int x[8] = { 1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304823, 962880562, 895706419 };
	int i, j;
	
	for (i = 0; i < 8; i++)
		for (j = 0; j < 4; j++)
			flag[i * 4 + j] = ((char*)(x + i))[3 - j];
	puts(flag);
	return 0;
}
```
C의 경우 포인터를 이용하면 손쉽게 언패킹을 할 수 있으며, 한 가지 유의할 점은 x86과 AMD64 아키텍쳐는 리틀 엔디언으로 바이트 정렬을 한다는 것이다. 따라서 위와같이 거꾸로 넣어주어야 한다.  

flag: `picoCTF{A_b1t_0f_b1t_sh1fTiNg_d79dd25ce3}`
