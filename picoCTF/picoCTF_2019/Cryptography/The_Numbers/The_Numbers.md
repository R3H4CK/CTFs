# The Numbers
> The numbers... what do they mean?

## Summary
* modified caesar cipher
* classical cipher

## Analysis
``` python
flag = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
result = []

for n in flag:
    result.append(n % 26)
    
if flag == result:
    print("Hello, world!")
```

## Solve
``` python
flag = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

for i in range(len(flag)):
    flag[i] = chr(flag[i] + 65 - 1)
flag.insert(7, '{')
flag.append('}')
print(''.join(flag))
```
변형된 시저 암호(modified caesar cipher)로 이는 2006년 이탈리아 경찰이 종이쪽지에 쓰인 암호문을 해독해서 마피아 두목을 체포했던 사례와 같은 방식의 암호를 사용한다.  

flag: `PICOCTF{THENUMBERSMASON}`
