# The Mueller Report
<blockquote>
20 points, 770 solves  
The redacted version of the Mueller report was finally released this week! There's some pretty funny stuff in there, but maybe the report has more beneath the surface.  
  
Author: SirIan
</blockquote>

## Summary
* hex editor
* Steganograpy

## Solve
``` python
with open("full-mueller-report.pdf", "rb") as f:
	flag = f.read()

flag = flag[flag.index(b'actf{'):]
flag = flag[:flag.index(b'}')+1]
print(flag.decode())
```

flag: `actf{no0o0o0_col1l1l1luuuusiioooon}`
