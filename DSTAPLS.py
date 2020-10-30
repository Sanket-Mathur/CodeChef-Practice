for _ in range(int(input())):
    N, K = map(int, input().split())
    print('NO' if (N//K)%K == 0 else 'YES')
