from sys import stdin, stdout
from math import gcd, sqrt

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    g = L[0]
    for i in L:
        g = gcd(g,i)
    if g == 1:
        stdout.write('-1\n')
    else:
        for i in range(2, int(sqrt(g)) + 1):
            if g % i == 0:
                stdout.write('{}\n'.format(i))
                break
        else:
            stdout.write('{}\n'.format(g))
