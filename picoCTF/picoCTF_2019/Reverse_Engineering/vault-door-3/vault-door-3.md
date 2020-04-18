# vault-door-3
> This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java

## Summary
* Java
* decompile

## Analysis
``` python
flag = "jU5t_a_sna_3lpm13gc49_u_4_m0rf41"

print(len(flag))
print(flag)

for i in range(0, 8):
    print(i, end=' ')
print()

for i in range(i + 1, 16):
    print(23 - i, end=' ')
print()

for i in range(i + 1, 32, 2):
    print(46 - i, end=' ')
print()

for i in range(31, 17, -2):
    print(i, end=' ')
print()
```

## Solve
``` python
flag = ['\000' for i in range(32)]
buffer = "jU5t_a_sna_3lpm13gc49_u_4_m0rf41"

for i in range(8):
    flag[i] = buffer[i]

for i in range(i + 1, 16):
    flag[i] = buffer[23 - i]

for i in range(i + 1, 32, 2):
    flag[i] = buffer[46 - i]

for i in range(17, 32, 2):
    flag[i] = buffer[i]
    
print(''.join(flag))
```
인덱스를 바꿔서 buffer에 넣어주는데 이를 다시 반대로 하면 된다.  

flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_90cf31}`
