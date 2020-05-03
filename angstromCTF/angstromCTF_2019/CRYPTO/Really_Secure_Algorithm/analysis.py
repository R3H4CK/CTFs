def gcd(a, b):
    while b:
        c = a % b
        a = b
        b = c
    return a

def xgcd(a, b):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while b:
        q, r = a // b, a % b
        s = s0 - q * s1
        t = t0 - q * t1
        a, b = b, r
        s0, s1 = s1, s
        t0, t1 = t1, t
    return a, s0, t0

def phi(n):
    totient = 0
    for k in range(n + 1):
        if gcd(k, n) == 1:
            totient += 1
    return totient


p, q = 5, 11
n = p * q
totient = phi(n) # phi(n) == (p - 1) * (q - 1)
m = 14
e = 7
if gcd(e, totient) != 1:
    exit(1)
d = xgcd(e, totient)[1]
if d < 0:
    d += totient
if e * d % totient != 1:
    exit(1)
c = pow(m, e, n)
if m == pow(c, d, n):
    print("Hello, world!")
