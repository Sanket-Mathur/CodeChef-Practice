from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, K = map(int, stdin.readline().split())
    L = list(map(int, stdin.readline().split()))
    
    maxEle = max(L)
    cnt = 0

    for i in range(K-1, N):
        if L[i] == maxEle:
            cnt += N - i
    
    stdout.write(f'{cnt}\n')