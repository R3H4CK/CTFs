# be-quick-or-be-dead-2

## Summary
* algorithm
* Fibonacci number

## Solution

``` c
#include <stdio.h>

char flag[58] = { 0x32, 0x23, 0x0b, 0xaf, 0, 0x1e, 0x2e, 0xbb, 0x30, 0x22, 0x0d, 0x9f, 0x23, 0x23, 0x0a, 0xaf, 0x28, 0x2b, 0x0b, 0xa3, 0x2f, 0x15, 0x1b, 0xa5, 0x39, 0x3f, 0x0d, 0xae, 0x2a, 0x2f, 0x37, 0xa3, 0x2b, 0x24, 0x37, 0xa2, 0x2e, 0x15, 0x0c, 0xaf, 0x22, 0x2f, 0x37, 0xa6, 0x2c, 0x39, 0x1c, 0x9f, 0x76, 0x72, 0x0e, 0xf3, 0x7e, 0x2c, 0x5c, 0xf8, 0x2d, 0 };
int key;

int fib(const int n)
{
	int* f;
	int i;
	f = (int*)malloc(n * sizeof(int));
	f[0] = 0;
	f[1] = 1;
	for (i = 2; i <= n; i++)
		f[i] = f[i - 1] + f[i - 2];
	return f[n];
}

int main(void)
{
	int i;
	key = fib(0x43b);

	for (i = 0; i < 57; i++)
	{
		flag[i] ^= ((char*)&key)[i % 4];
		if (i % 4 == 3)
			key++;
	}
	puts(flag);
	return 0;
}
```
IDA로 Hex-Rays를 적용한 소스를 보면 1처럼 시그널을 호출하고 복호화 루틴을 거치게 된다. 복호화 루틴에서 피보나치 수를 사용하는데 재귀함수로 구현되어 있기 때문에 계산하는데 시간이 너무 오래걸린다.  
<a href="https://ko.numberempire.com/fibonaccinumbers.php">피보나치 수</a>(Fibonacci number)는 F<sub>0</sub>=0, F<sub>1</sub>=1, F<sub>n</sub>=F<sub>n-1</sub>+F<sub>n-2</sub>와 같이 재귀적으로 정의되는 수다. 피보나치 수를 계산하거나 위의 소스처럼 fib 함수를 반복문으로 고쳐서 실행하면 된다.

flag: `picoCTF{the_fibonacch_sequence_can_be_done_fast_88f31f48}`
