# Time's Up, For the Last Time!
> You've solved things fast. You've solved things faster! Now do the impossible. times-up-one-last-time, located in the directory at /problems/time-s-up--for-the-last-time-_1_a7830af9d51a361ee5d3b9eece69c22f.

## Summary
* signal
* /dev/urandom
* ((char*)&n)[i]

## Analysis
``` python
from ctypes import *
from os import urandom
from sys import byteorder

libc = CDLL("libc.so.6")

guess = c_int()
result = c_int()

def init_randomness():
    libc.srand(libc.time(None))

def get_random():
    return c_int(int.from_bytes(urandom(8), byteorder))

def get_random_op():
    # v4 : v3 : v2
    v2 = 11119202356222773194984351477035
    v0 = libc.rand()
    return c_uint(v2 >> (v0 - 13 * ((0x4EC4EC4EC4EC4EC5 * v0 >> 64) >> 2)) * 8 & 0xff)

def do_op(a, b, c):
    try:
        return c_int({
            '%': b % c if c else b,
            '&': c & b,
            '*': c * b,
            '+': b + c,
            '-': b - c,
            '/': b / c if c else b,
            '^': c ^ b,
            'f': b,
            'o': c,
            'r': c,
            't': b,
            'x': c,
            '|': c | b
        }[chr(a)])
    except KeyError:
        exit(1)

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
        print("(%d)" % v1, end='')
        return c_int(v1)

def generate_challenge():
    global result
    result = gen_expr(4)


init_randomness()
print("Challenge: ", end='')
generate_challenge()
print(flush=True)
print("Setting alarm...", flush=True)
libc.ualarm(10, 0)
print("Solution? ", end='')
libc.scanf(b"%d", pointer(guess))

if guess.value == result.value:
    print("Congrats! Here is the flag!")
    libc.system("/bin/cat flag.txt")
else:
    print("Nope!")
```

## Solve
``` python
from ctypes import *
import subprocess

libc = CDLL("libc.so.6")

SIGALRM = 14
SIG_BLOCK = 0

class sigset_t(Structure):
    _fields_= [("__sigbit", c_uint * 4)]


sigset = sigset_t()

libc.sigemptyset(pointer(sigset))
libc.sigaddset(pointer(sigset), SIGALRM)
libc.sigprocmask(SIG_BLOCK, pointer(sigset), None)

while True:
    p = subprocess.Popen("./times-up-one-last-time", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.stdin.write('0\n')
    flag = p.stdout.read()
    if "pico" in flag:
        print(flag)
        break
```
이 문제의 의도는 C 언어에서 subprocess를 이용하는 것으로 보이지만 time-xxx 문제들은 모두 시그널을 Block 시켜서 풀 수 있다. 또한 주어진 식의 결과는 `/`, `%`와 같은 연산 때문에 정수 범위에서는 0이 나올 확률이 상당히 높다.  

flag: `picoCTF{And now you can hack time! #2e0a37d1}`
