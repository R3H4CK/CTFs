# assembly-0

## Summary
* 80x86 Assembly
* decompile

## Solution
``` assembly
.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]
	mov	ebx,DWORD PTR [ebp+0xc]
	mov	eax,ebx
	mov	esp,ebp
	pop	ebp	
	ret
```

위의 소스를 C로 디컴파일하면 다음과 같다.

``` c
int asm0(int a, int b)
{
	int tmp = b;	
	return tmp;
}
```

따라서 asm0(0xc9,0xb0)는 bxb0을 반환한다.

flag: `0xb0`
