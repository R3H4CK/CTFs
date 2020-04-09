# assembly-3
> What does asm3(0xfac0f685,0xe0911505,0xaee1f319) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-3_1_10d10207229f8f1cdf9d458cfdb0304e.

## Summary
* 80x86 Assembly
* excution

## Analysis
``` assembly
push   	ebp
mov    	ebp,esp            ; enter
mov	eax,0x27               ; eax=0
xor	al,al                  ; al=0
mov	ah,BYTE PTR [ebp+0xb]  ; ah=*((char*)ebp+0xb)
sal	ax,0x10                ; ax <<= 0x10
sub	al,BYTE PTR [ebp+0xc]  ; al -= *((char*)ebp+0xc) 
add	ah,BYTE PTR [ebp+0xf]  ; ah += *((char*)ebp+0xf)
xor	ax,WORD PTR [ebp+0x12] ; ax += *((short*)ebp+0x12)
mov	esp, ebp
pop	ebp                    ; leave
ret
```

## Solve
``` assembly
.486
.model flat, c

include kernel32.inc
include msvcrt.inc

includelib kernel32.lib
includelib msvcrt.lib

.data
format byte "0x%x", 10, 0 

.code
asm3 proc
	push ebp	
	mov ebp, esp	
	mov	eax,39
	xor al, al
	mov	ah, BYTE PTR [ebp+11]
	sal ax, 16
	sub al, BYTE PTR [ebp+12]
	add ah, BYTE PTR [ebp+15]	
	xor ax, WORD PTR [ebp+18]	
	mov	esp, ebp	
	pop	ebp	
	ret
asm3 endp

start:
	push 2934043417
	push 3767604485
	push 4206950021
	call asm3
	push eax
	push offset format
	call crt_printf
	push 5000
	call Sleep
	push 0
	call ExitProcess
end start	
```
주어진 소스를 프로시저로 작성해서 asm3(0xfac0f685, 0xe0911505, 0xaee1f319)로 호출하면 된다.  

flag: `0x4e1a`
