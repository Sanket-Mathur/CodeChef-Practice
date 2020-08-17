try:
    for _ in range(int(input())):
        N, M = map(int, input().split())
        print(N*(M-1) + M*(N-1))
except:
    pass
