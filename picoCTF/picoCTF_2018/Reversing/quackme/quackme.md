# quackme

## Summary
* XOR
* simple encryption

## Solution
``` python
flag = ""
greetingMessage = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"
sekrutBuffer = ")\x06\x16O+50\x1eQ\x1b[\x14K\x08]+S\x10TQCM\T]"

for i in range(25):
    flag += chr(ord(sekrutBuffer[i]) ^ ord(greetingMessage[i]))
print(flag)
```
IDA로 Hex-Rays 해서 소스를 확인한 다음 위와 같은 역산하는 코드를 작성하면 된다.  

flag: `picoCTF{qu4ckm3_6b15c941}`
