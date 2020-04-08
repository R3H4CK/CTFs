# assembly-1
> What does asm1(0x15e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-1_3_cfc4373d0e723e491f368e7bcc26920a.

## Surmmary
* 80x86 Assembly
* Hand-Rays

## Analysis
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
주어진 어셈블리 소스를 Hand-Rays하면 위와 같으므로 asm1(0x15e)는 0x161을 반환한다.

flag: `0x161`
