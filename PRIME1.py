from sys import stdin, stdout
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n))+1, 2):
            if n % i == 0:
                return False
    return True

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    for i in range(n, m+1):
        if isPrime(i):
            stdout.write(f'{i}\n')
    stdout.write('\n')
