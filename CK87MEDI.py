try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        L = sorted(map(int, input().split()))
        print(L[(N+K) // 2])
except:
    pass
