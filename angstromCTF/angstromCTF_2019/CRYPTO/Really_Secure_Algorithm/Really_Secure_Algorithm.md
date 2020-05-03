# Really Secure Algorithm
<blockquote>
30 points, 593 solves  
I found this flag somewhere when I was taking a walk, but it seems to have been encrypted with this Really Secure Algorithm!  
  
Author: lamchcl
</blockquote>

## Analysis
``` python
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
```

## Solve
``` python
p = 8337989838551614633430029371803892077156162494012474856684174381868510024755832450406936717727195184311114937042673575494843631977970586746618123352329889
q = 7755060911995462151580541927524289685569492828780752345560845093073545403776129013139174889414744570087561926915046519199304042166351530778365529171009493
e = 65537
c = 7022848098469230958320047471938217952907600532361296142412318653611729265921488278588086423574875352145477376594391159805651080223698576708934993951618464460109422377329972737876060167903857613763294932326619266281725900497427458047861973153012506595691389361443123047595975834017549312356282859235890330349

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
    return (a, s0, t0)

def phi(n):
    totient = 0
    for k in range(1, n + 1):
        if gcd(k, n) == 1:
            totient += 1
    return totient


n = p * q
totient = (p - 1) * (q - 1)
d = xgcd(e, totient)[1]
if d < 0:
    d += totient
m = pow(c, d, n)
print(m)
```
간단한 RSA(Rivest-Shamir-Adleman) 문제인데 p, q와 공개 지수 e가 주어져 있으므로 확장 유클리드 알고리즘(extended Euclidean algorithm)을 이용하여 비밀 지수 d를 구한다. 그리고 복호화 알고리즘을 적용하면 된다.  

flag: `actf{really_securent_algorithm}`
