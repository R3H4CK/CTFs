# assembly-0
> What does asm0(0xc9,0xb0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-0_4_0f197369bfc00a9211504cf65ac31994.

## Summary
* 80x86 Assembly
* decompile

## Analysis
``` c
int asm0(int a, int b)
{
	int tmp = b;	
	return tmp;
}
```
주어진 어셈블리 소스를 직접 디컴파일하면 위의 소스와 같으므로 asm0(0xc9,0xb0)는 bxb0을 반환한다.

flag: `0xb0`
