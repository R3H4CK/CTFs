``` batch
nc 2018shell.picoctf.com 14390
```

nc로 접속해서 나오는 값을 https://www.asciitohex.com/ 에서 변환하여 주어진 시간 안에 입력하면 된다. 또는 pwntools를 사용할 수 있다.

``` python

from pwn import *

sh = remote("2018shell.picoctf.com", 14390)

data = unbits(sh.recvuntil("Input:\n").split('\n')[-4][19:-11].replace(' ', ''))
sh.sendline(data)

data = unhex(sh.recvuntil("Input:\n").split('\n')[-3][19:-11])

data = sh.recvuntil("Input:\n").split('\n')[-3][20:-11]
data = ''.join([chr(int(i, 8)) for i in data.split(' ')])
sh.sendline(data)

print(sh.recv())
```
