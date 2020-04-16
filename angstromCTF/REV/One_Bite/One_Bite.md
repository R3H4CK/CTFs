# One Bite
> Whenever I have friends over, I love to brag about things that I can eat in a single bite. Can you give this program a tasty flag that fits the bill?  
/problems/2019/one_bite  
Author: SirIan

## Summary
* XOR
* simple encryption

## Solve
``` python
flag = ""
table = "]_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA"

for ch in table:
    flag += chr(ord(ch) ^ 0x3C)
print(flag)
```

flag: `actf{i_think_im_going_to_be_sick}`
