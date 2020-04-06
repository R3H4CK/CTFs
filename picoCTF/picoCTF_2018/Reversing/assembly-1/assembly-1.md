# assembly-1

## Surmmary
* 80x86 Assembly
* Hand-Rays

## Solution
``` Assembly
.intel_syntax noprefix
.bits 32
	
.global asm1

asm1:
	push	ebp
	mov	ebp,esp
	cmp	DWORD PTR [ebp+0x8],0xdc
	jg 	part_a	
	cmp	DWORD PTR [ebp+0x8],0x8
	jne	part_b
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x68
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
	cmp	DWORD PTR [ebp+0x8],0xfc
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp
	ret
```

위의 소스를 Hand-Rays(지금부터 손으로 디컴파일 하는 것을 Hand-rays라고 하겠습니다)하면 다음과 같다.

``` c
int asm1(int a)
{
	if (a <= 0xdc)
		if (a == 0x8)
			return a + 0x3;
		else
		{
			return a - 0x3;
			if (a == 0xfc)
				return a - 0x3;
			else
				goto part_c;
		}
	else if (a == 0x68)
		return a - 0x3;
	else
part_c:
		return a + 0x3;
}
```

따라서 asm1(0x15e)는 0x161을 반환한다.  

flag: `0x161`
