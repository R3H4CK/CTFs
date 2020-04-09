# assembly-4
> Can you find the flag using the following assembly source? WARNING: It is VERY long...

## Summart
* 80x86 Assembly
* NASM

## Solve
``` bash
nasm -f elf32 comp.nasm
gcc -m32 comp.o -o comp
./comp; echo "}"
```
문제에서 설명하는 것 처럼 소스가 매우 길다. 그냥 리눅스 환경에서 nasm이므로 리눅스 환경에서 어셈블하고 실행하면 된다.

flag: `picoCTF{1_h0p3_y0u_c0mP1l3d_tH15_32429699163}`
