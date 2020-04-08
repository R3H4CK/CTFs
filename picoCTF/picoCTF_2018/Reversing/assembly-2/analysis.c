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
