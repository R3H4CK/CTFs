# assembly-2

## Summary
* 80x86 Assembly
* GNU Compiler C Loop(for or while)

## Solution
``` assembly
.intel_syntax noprefix
.bits 32
	
.global asm2

asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD PTR [ebp+0xc]
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8]
	mov	DWORD PTR [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1
	add	DWORD PTR [ebp+0x8],0x76
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0xa1de
	jle    	part_a
	mov    	eax,DWORD PTR [ebp-0x4]
	mov	esp,ebp
	pop	ebp
	ret
```

위의 소스는 GNU C 컴파일러의 while문의 형태를 보여주고 있다. Hand-Rays하면 다음과 같다.

``` c
int asm2(int a, int b)
{
	int i = b;
	int n = a;
	
	while (i <= 0xa1de)
	{
		i++;
		b += 0x76;
	}
	return i;
}
```

따라서 asm2(0x7, 0x28)의 반환 값은 0xa1df이다.  

flag: `0xa1df`
