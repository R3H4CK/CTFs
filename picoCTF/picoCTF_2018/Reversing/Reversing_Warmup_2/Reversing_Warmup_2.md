# Reversing Warmup 2
## Summary
* base64
* misc

## Solution
> dGg0dF93NHNfczFtcEwz

주어진 문자열을 base64 decode 하면 된다.

``` python
import base64

print(str(base64.b64decode("dGg0dF93NHNfczFtcEwz"), encoding='utf-8'))
```
  
flag: 'picoCTF{th4t_w4s_s1mpL3}'
