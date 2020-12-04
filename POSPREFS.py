for _ in range(int(input())):
    N, K = map(int, input().split())
    L = []
    for i in range(1, K+1):
        if sum(L) > i:
            L.append(-i)
        else:
            L.append(i)
    if N > K:
        if sum(L) - K+1 > 0:
            L[-1] = -L[-1]
            L.append(K+1)
        else:
            L.append(-(K+1))
    for i in range(K+2, N+1):
        L.append(-i)
    print(*L)
