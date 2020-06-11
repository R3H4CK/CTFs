# Magic Number
<blockquote>
Magic Number  
author : Kong  
point : 500  
solvers : 1  
  
Magic Number  
Monkey Magic~  
--Kong
</blockquote>

## Summary
* C++ Binary
* Z3

## Analysis
``` python
def check(s, n):
    s = list(s)
    if n < 11:
        magic = 0
        for i in range(n - 1, -1, -1):
            for j in range(0, 10**(n-i-1)):
                magic += ord(s[i]) - 48
        if magic % n:
            return 0
        else:
            return check(s, n + 1)
    else:
        return 1


magic_number = input("Input a Magic Number : ")
if len(magic_number) == 10:
    print("Checking.... Plz Wait!", end='')
    tmp = check(magic_number, 1)
    if tmp:
        print(tmp)
        for i in range(len(magic_number)):
            for j in range(0, i):
                if magic_number[i] == magic_number[j]:
                    print("Ganbare!!! ", end='')
                    exit(0)
        print("Great! The Flag is... HCAMP{", end='')
        print("flag", end='}')
    else:
        print("Melong@~@!", end='')
        exit(0)
else:
    print("No!", end='')
    exit(0)
```

Solve
``` python
analysis의 소스를 보면 `Magic Number`의 길이가 10이면 check 함수를 거친다. 그다음 함수의 반환값이 참이면 `Magic Number`의 자릿수별로 중복되는 값이 없는지 검사한다. 연산이 상당히 크므로 직접 계산하기는 어렵다. 따라서 check를 z3에서의 식으로 정의하고 계산하면 된다.
flag: `작성중`
```
