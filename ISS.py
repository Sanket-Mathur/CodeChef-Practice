from sys import stdin, stdout
from math import gcd

for _ in range(int(stdin.readline())):
    k = int(stdin.readline())
    g = 0
    for i in range(1, 2*k+1):
        g += gcd(k + pow(i, 2), k + pow(i+1, 2))
    
    stdout.write(f'{g}\n')
