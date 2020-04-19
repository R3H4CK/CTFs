# vault-door-5
> In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: VaultDoor5.java

## Summary
* base64
* url

## Solve
``` python
import base64
from urllib import parse

flag = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY0JTYyJTM2JTM5JTM0JTM2JTYyJTYx"

flag = str(base64.b64decode(flag), 'utf-8')
flag = str(parse.unquote(flag))

print(flag)
```
입력 값을 base64와 url로 encode해서 값이 맞는지 flag를 encode한 값과 비교하므로 그냥 그대로 decode하면 된다.

flag: `picoCTF{c0nv3rt1ng_fr0m_ba5e_64_db6946ba}`
