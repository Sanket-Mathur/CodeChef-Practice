from sys import stdin, stdout
from math import gcd

for _ in range(int(stdin.readline())):
    a, b, n = map(int, stdin.readline().split())
    if a == b:
        g = 2 * pow(a, n)
    else:
        g = gcd(pow(a, n, a-b) + pow(b, n, a-b), a-b)
    stdout.write('{}\n'.format(g % 1000000007))
