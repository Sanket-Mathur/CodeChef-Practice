def gcd(a, b):
    if a == 0:
        return b 
    return gcd(b%a, a)

for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    g = gcd(L[0], L[1])
    for i in range(2,N):
        g = gcd(g, L[i])
    print(0 if g == 1 else -1)
