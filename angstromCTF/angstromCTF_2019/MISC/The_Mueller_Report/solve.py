with open("full-mueller-report.pdf", "rb") as f:
	flag = f.read()

flag = flag[flag.index(b'actf{'):]
flag = flag[:flag.index(b'}')+1]
print(flag.decode())
