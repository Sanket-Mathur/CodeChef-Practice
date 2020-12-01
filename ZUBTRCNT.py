for t in range(int(input())):
    N, K = map(int, input().split())
    if N < K:
        print('Case {}: {}'.format(t+1, 0))
    else:
        n = N-K+1 
        print('Case {}: {}'.format(t+1, n*(n+1) // 2))
