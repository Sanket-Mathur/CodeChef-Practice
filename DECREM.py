from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    l, r = map(int, stdin.readline().split())
    if l*2 <= r:
        stdout.write('-1\n')
    else:
        stdout.write(f'{r}\n')
