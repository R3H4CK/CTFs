# Hello Mach!
> Welcome the Mach-O world.  
This Architecture is very specific File Signature.  
Can you running?  
--c0nstant

## Summary
* Mach-O
* File Signatures

## Solve
``` python
table = "BIKGZq]9fi:goUGkib'EUb>iaoxyw"

for i in range(0xff):
    flag = ""
    for ch in table:
        flag += chr(ord(ch) ^ i)
    print(i, flag)
    if flag[:5] == "HCAMP":
        break
```
문제를 다운받으면 runplz라는 이름의 폴더 안에 문제 파일이 있는데 이는 문제를 실행시켜야 하는 것으로 생각할 수 있다.  
HxD로 열어보면 파일 시그니처는 `DE AD BE EF`로 mach-o 형식이 아니라서 실행이 되지 않는다. 이를 `CF FA ED FE`로 바꾸고 실행하면 flag를 얻을 수 있다.  
그런데 현재 MacOS 환경이 없다면 실행할 수 없다. IDA로 String window를 보면 암호화된 flag처럼 보이는 문자열이 있는데 이를 [0, 255) 구간에서 XOR하도록(게싱) 브루트 포스하면 10에서 flag를 구할 수 있다.  

flag: `HCAMP{W3lc0me_Mach-O_h4ckers}`
