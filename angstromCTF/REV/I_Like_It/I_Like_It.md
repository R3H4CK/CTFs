# I Like It
> Now I like dollars, I like diamonds, I like ints, I like strings. Make Cardi like it please.  
  
> `/problems/2019/i_like_it`  
  
> Author: SirIan

## Summary
* input
* strcmp

## Solve
``` python
from z3 import *

x, y = Ints('x y')

solve(x + y == 136, x * y == 3783, x < y)
```

`` bash
(python -c 'print "39 97"';cat)|(python -c 'print "okrrrrrrr"';cat)|./i_like_it
```

flag: `actf{okrrrrrrr_39_97}`
