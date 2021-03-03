from sys import stdin, stdout
from math import ceil

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    time = 0
    for i in range(N):
        x, l, f = map(int, stdin.readline().split())
        if time <= x:
            time = x+l
        else:
            time = ceil((time-x) / f)*f + x + l
    stdout.write('{}\n'.format(time))
