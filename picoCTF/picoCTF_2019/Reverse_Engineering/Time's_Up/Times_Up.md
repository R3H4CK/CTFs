# Time's Up
> Time waits for no one. Can you solve this before time runs out? times-up, located in the directory at /problems/time-s-up_5_44ffbb55dd7707c9e13da8551841f850.

## Summary
* signal
* random number

## Analysis
``` python
from ctypes import *

libc = CDLL("libc.so.6")

seed = c_int()
result = c_int()
guess = c_int()

def init_randomness():
    libc.srand(libc.time(None))
    global seed
    seed.value = libc.rand() * libc.rand() + libc.rand()

def get_random():
    global seed
    seed.value *= libc.rand()
    seed.value += libc.rand()
    seed.value *= 1337
    seed.value += libc.rand()
    return c_int(libc.rand() * seed.value)

def get_random_op():
    v1 = 11563
    return c_uint(v1 >> (get_random().value & 1) * 8 & 0xff)

def do_op(a, b, c):
    if a == 43:
        return c_int(b + c)
    if a != 45:
        exit(1)
    return c_int(b - c)

def maybe_decrease(n):
    return c_int(n) if libc.rand() % 50 <= 0 else c_int(n - 1)

def gen_expr(n):
    if n:
        v3 = maybe_decrease(n).value
        v4 = maybe_decrease(n).value
        v5 = get_random_op().value
        print('(', end='')
        v6 = gen_expr(v3).value
        print(" %c " % chr(v5), end='')
        v7 = gen_expr(v4).value
        print(')', end='')
        return do_op(v5, v6, v7)
    else:
        v1 = get_random().value
        print("%d" % v1, end='')
        return c_int(v1)

def generate_challenge():
    global result
    result.value = gen_expr(4).value


init_randomness()
print("Challenge: ", end='')
generate_challenge()
print(chr(10), end='', flush=True)
print("Setting alarm...", flush=True)
libc.alarm(5)
print("Solution? ", end='')
libc.scanf(b"%lld", pointer(guess))

if guess.value == result.value:
    print("Congrats! Here is the flag!")
    libc.system("/bin/cat flag.txt")
else:
    print("Nope!")
```

## Solve
``` python
from pwn import *

p = process("./times-up")

expr = p.recv()
expr = expr[len('Challenge: '):expr.index('\n')]

p.sendline(str(eval(expr)))

print(p.recvall())
```
서버 쉘의 해당 경로에서 실행하면 5초 뒤에 SIGALARM을 발생시켜 종료하는데 이는 pwntools를 사용하면 쉽게 풀 수 있다.  
home 디렉토리에서 solve.py를 작성한 후 다시 해당 경로로 이동해서 python으로 실행하면 된다.  
``` python
import subprocess

p = subprocess.Popen("./times-up", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
expr = p.stdout.readline()[10:-1]
expr = eval(expr)
p.stdin.write(str(expr)+'\n')
print(p.stdout.read())
```
다른 방법으로는 subprocess 모듈을 이용하여 자식 프로세스에 접근하는 방식으로 풀 수 있다.  

flag: `picoCTF{Gotta go fast. Gotta go FAST. #3c4b5166}`
