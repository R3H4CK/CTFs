# assembly-2
> What does asm2(0x7,0x28) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-2_4_f8bfecf223768f4cac035751390ea590.

## Summary
* 80x86 Assembly
* GNU C Compiler Loop(for or while)

## Analysis
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
주어진 어셈블리 소스는 임의로 작성한 것으로 보이지만 GNU C 컴파일러의 while 루프에 가깝다.  
주어진 소스를 Hand-Rays하면 위와 같으므로 asm2(0x7, 0x28)의 반환 값은 0xa1df이다.  

flag: `0xa1df`
