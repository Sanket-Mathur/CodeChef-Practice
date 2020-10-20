for _ in range(int(input())):
    N, K, L = map(int, input().split())
    if K*L < N:
        print(-1)
    elif K == 1 and N > 1:
        print(-1)
    else:
        l = []
        for i in range(K):
            l.append(i+1)
        l = l*L 
        print(*l[:N])
