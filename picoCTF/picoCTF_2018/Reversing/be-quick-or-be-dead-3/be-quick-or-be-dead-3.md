# be-quick-or-be-dead-3

## Summary
* algorithm
* DP(Dynamic Programming)

## Solution
``` c
#include <stdio.h>

char flag[42] = { 0x0AE, 0x1B, 0x48, 0x96, 0x9C, 0x26, 0x6D, 0x82, 0x84, 0x0B, 0x45, 0x98, 0x8C, 0x1B, 0x48, 0x0A6, 0x92, 0, 0x1B, 0x9E, 0x91, 0x13, 0x46, 0x94, 0x8D, 0x1C, 0x4C, 0x0A6, 0x83, 0x6, 0x5C, 0x0A6, 0x82, 0x43, 0x49, 0x0CD, 0x86, 0x4B, 0x1A, 0x0CB, 0x95, 0 };
unsigned int key;

unsigned int calc(int n)
{
	static unsigned int cal[0x18E28];
	int i;

	for (i = 0; i <= n; i++)
	{
		if (i > 4)
			cal[i] = cal[i - 1] - cal[i - 2] + cal[i - 3] - cal[i - 4] + 0x1234 * cal[i - 5];
		else
			cal[i] = i * i + 0x2345;
	}
	return cal[n];
}

int main(void)
{
	int i;
	key = calc(0x18E28);
	
	for (i = 0; i < 41; i++)
	{
		flag[i] ^= ((char*)&key)[i % 4];
		if (i % 4 == 3)
			key++;
	}
	puts(flag);
	return 0;
}
```
IDA로 Hex-Rays해서 calc 함수의 소스를 보면 4를 기점으로 함수의 정의가 다른데 이는 수학적으로는 조각적으로 정의된 함수(piecewise-defined function)입니다.  
재귀호출로 구현되어 있어 너무 느려서 계산을 할 수 없다. 이를 반복문으로 고쳐서 위와 같이 복호화 루틴을 거쳐주면 된다.  

flag: `picoCTF{dynamic_pr0gramming_ftw_d1b4a912}`
