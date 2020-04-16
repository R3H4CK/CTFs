from z3 import *

x, y = Ints('x y')

solve(x + y == 136, x * y == 3783, x < y)
