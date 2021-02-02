from math import gcd
for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    g = gcd(L[0], L[1])
    for i in range(2,len(L)):
        g = gcd(g, L[i])
    print(g)
