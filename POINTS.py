from math import sqrt
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    stdin.readline()
    N = int(stdin.readline())
    L = [tuple(map(int, stdin.readline().split())) for i in range(N)]
    L.sort(key=lambda x: (x[0], -x[1]))
    
    dist = 0.0
    for i in range(N-1):
        dist += sqrt((L[i][0] - L[i+1][0])**2 + (L[i][1] - L[i+1][1])**2)
    stdout.write('{:.2f}\n'.format(dist))
