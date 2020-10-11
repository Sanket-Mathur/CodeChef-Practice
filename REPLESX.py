for _ in range(int(input())):
    N, X, p, k = map(int, input().split())
    A = sorted(map(int, input().split()))
    if A[p-1] == X:
        print(0)
    elif k >= p and A[p-1] >= X:
        c = 0
        i = p-1 
        while i >= 0 and A[i] > X:
            c += 1 
            i -= 1 
        print(c)
    elif k <= p and A[p-1] <= X:
        c = 0
        i = p-1
        while i < N and A[i] < X:
            c += 1 
            i += 1 
        print(c)
    else:
        print(-1)
