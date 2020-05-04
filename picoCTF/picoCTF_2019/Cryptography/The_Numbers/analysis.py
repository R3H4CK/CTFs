flag = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
result = []

for n in flag:
    result.append(n % 26)
    
if flag == result:
    print("Hello, world!")
