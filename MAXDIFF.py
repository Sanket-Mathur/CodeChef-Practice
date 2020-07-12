for _ in range(int(input())):

    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    cN = min(K, N-K)
    
    A = 0
    for i in range(cN):
        m = min(L)
        L.remove(m)
        A += m
    
    print(sum(L) - A)