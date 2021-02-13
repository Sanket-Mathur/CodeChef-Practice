N, K = map(int, input().split())
L = list(map(int, input().split()))

if K == 0:
    print(*L)
else:
    K = 1 if K % 2 else 2
    for i in range(K):
        m = max(L)
        for j in range(N):
            L[j] = m - L[j]
    print(*L)
