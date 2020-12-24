for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    c1 = c2 = 0
    for i in range(N-1):
        if A[i] > A[i+1]:
            c1 += 1 
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                c2 += 1 
    print('YES' if c1 == c2 else 'NO')
