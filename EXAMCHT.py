from sys import stdin, stdout
from math import sqrt

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    if a == b:
        stdout.write('-1\n')
    else:
        d = set()
        n = abs(a-b)
        for i in range(1, int(sqrt(n)) + 1): 
            if n % i == 0:
                d.add(i)
                d.add(n // i)
        stdout.write(f'{len(d)}\n')
