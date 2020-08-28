for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N 
    for i in range(N):
        c = 0
        for j in A:
            if j > A[i]:
                c += 1 
        B[i] = c
    print(*B)
