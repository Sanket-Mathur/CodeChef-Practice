try:
    N = int(input())
    L = []
    for _ in range(N):
        x = int(input())
        L.append(x)
    L.sort()
    P = []
    for i in L:
        P.append(i * N)
        N -= 1
    print(max(P))
except:
    pass
