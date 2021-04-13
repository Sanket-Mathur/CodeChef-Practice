from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, M, K = map(int, stdin.readline().split())
    N, M = N+1, M+1
    L = [[0] * M] + [[0] + list(map(int, stdin.readline().split())) for i in range(N-1)]
        
    cnt = 0
    if M == 2:
        for i in range(1,N):
            if L[i][1] >= K:
                cnt += 1 
    elif N == 2:
        for j in range(1,M):
            if L[1][j] >= K:
                cnt += 1 
    else:
        for i in range(1,N):
            for j in range(1,M):
                L[i][j] += L[i][j-1]
        for j in range(1,M):
            for i in range(1,N):
                L[i][j] += L[i-1][j]
        
        for l in range(1, min(N,M)):
            for i in range(l, N):
                for j in range(l, M):
                    if (L[i][j] + L[i-l][j-l] - L[i][j-l] - L[i-l][j]) / (l*l) >= K:
                        cnt += M-j
                        break
        
    stdout.write(f'{cnt}\n')
