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