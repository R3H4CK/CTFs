from ctypes import *
import signal
import os

msvcrt = CDLL("msvcrt.dll")

seed = c_longlong()
result = c_longlong()
guess = c_longlong()

def init_randomness():
    msvcrt.srand(msvcrt.time(None))
    global seed
    seed.value = msvcrt.rand() * msvcrt.rand() + msvcrt.rand()

def get_random():
    global seed
    seed.value *= msvcrt.rand()
    seed.value += msvcrt.rand()
    seed.value *= 1337
    seed.value += msvcrt.rand()
    return c_longlong(msvcrt.rand() * seed.value)

def get_random_op():
    v1 = 11563
    return c_uint(v1 >> (get_random().value & 1) * 8 & 0xff)

def do_op(a, b, c):
    if a == 43:
        return c_longlong(b + c)
    if a != 45:
        exit(1)
    return c_longlong(b - c)

def maybe_decrease(n):
    return c_int(n) if msvcrt.rand() % 50 <= 0 else c_int(n - 1)

def gen_expr(n):
    if n:
        v3 = maybe_decrease(n).value
        v4 = maybe_decrease(n).value
        v5 = get_random_op().value
        print(chr(40), end='')
        v6 = gen_expr(v3).value
        print(f" {chr(v5)} ", end='')
        v7 = gen_expr(v4).value
        print(chr(41), end='')
        return do_op(v5, v6, v7)
    else:
        v1 = get_random().value
        print("%d" % v1, end='')
        return c_longlong(v1)

def generate_challenge():
    global result
    result.value = gen_expr(4).value


init_randomness()
print("Challenge: ", end='')
generate_challenge()
print(chr(10), end='', flush=True)
print("Setting alarm...", flush=True)
signal.alarm(5)
print("Solution? ", end='')
msvcrt.scanf(b"%lld", pointer(guess))

if guess.value == result.value:
    print("Congrats! Here is the flag!")
    os.system("/bin/cat flag.txt")
else:
    print("Nope!")
