for _ in range(int(input())):
    N, M = map(int, input().split())
    L = sorted(map(int, input().split()), reverse=True)
    s = cnt = 0
    while s < M and cnt < len(L):
        s += L[cnt]
        cnt += 1 
    print(cnt if s >= M else -1)
