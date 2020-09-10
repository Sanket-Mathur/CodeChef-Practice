for _ in range(int(input())):
    N = int(input())
    res = [[0]*N for n in range(N)]
    start = 1 
    for i in range(N):
        for j in range(i+1):
            res[j][i-j] = start
            start += 1
    for i in range(1,N):
        for j in range(N-i):
            res[i+j][N-j-1] = start
            start += 1
    [print(*r) for r in res]
