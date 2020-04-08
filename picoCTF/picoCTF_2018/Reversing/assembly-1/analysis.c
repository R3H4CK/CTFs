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
