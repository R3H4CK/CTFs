#include <stdio.h>

int main(void)
{
	char flag[33] = "\0";
	int x[8] = { 1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304823, 962880562, 895706419 };
	int i, j;
	
	for (i = 0; i < 8; i++)
		for (j = 0; j < 4; j++)
			flag[i * 4 + j] = ((char*)(x + i))[3 - j];
	puts(flag);
	return 0;
}
