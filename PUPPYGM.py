from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    if a % 2 == 0 or b % 2 == 0:
        stdout.write('Tuzik\n')
    else:
        stdout.write('Vanka\n')
