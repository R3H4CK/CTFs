import subprocess

p = subprocess.Popen("./times-up", stdin=subprocess.PIPE, stdout=subprocess.PIPE)

expr = p.stdout.readline()[10:-1]
p.stdin.write(str(eval(expr))+'\n')

print(p.stdout.read())
