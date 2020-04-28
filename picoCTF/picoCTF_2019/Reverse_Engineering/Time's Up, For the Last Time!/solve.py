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
