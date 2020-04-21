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
