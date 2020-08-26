try:
    for _ in range(int(input())):
        N, K, V = map(int, input().split())
        L = list(map(int, input().split()))
        x = (V * (N+K)) - sum(L)
        if x % K == 0 and x > 0:
            print(x//K)
        else:
            print(-1)
except:
    pass
