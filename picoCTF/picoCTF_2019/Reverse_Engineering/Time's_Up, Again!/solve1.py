import subprocess

while True:
    p = subprocess.Popen("./times-up-again", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    expr = p.stdout.readline()[10:-1]
    try:
        p.stdin.write(str(eval(expr))+'\n')
    except IOError:
        continue
    flag = p.stdout.read()
    if "pico" in flag:
        print(flag)
        break
