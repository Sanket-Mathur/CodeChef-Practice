import numpy as np
from itertools import combinations
for _ in range(int(input())):
    N, M = map(int, input().split())
    L = []
    for i in range(N):
        x = list(map(int, list(input())))
        L.append(x)
    a = np.array(L).T
    c = 0
    for i in a:
        ones = i.sum()
        c += len(list(combinations(range(ones), 2)))
    print(c)
