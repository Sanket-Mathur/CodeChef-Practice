for _ in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    m = sum(L[0:K])
    for i in range(1,N-K+1):
        if sum(L[i:i+K]) > m:
            m = sum(L[i:i+K])
    print(m)
