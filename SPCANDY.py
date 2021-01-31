for _ in range(int(input())):
    N, K = map(int, input().strip().split())
    if K == 0:
        print(0, N)
    else:
        print(N//K, N%K)
