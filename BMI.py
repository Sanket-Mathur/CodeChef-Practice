from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    M, H = map(int, stdin.readline().split())
    BMI = M / H**2
    if BMI <= 18:
        stdout.write('1\n')
    elif BMI <= 24:
        stdout.write('2\n')
    elif BMI <= 29:
        stdout.write('3\n')
    else:
        stdout.write('4\n')
