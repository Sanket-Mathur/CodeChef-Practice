for _ in range(int(input())):
    N = int(input())
    G = []
    for i in range(N):
        G.append(input())
    cnt = 0
    row = [True] * N 
    col = [True] * N
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if G[i][j] == '#':
                row[i] = False
                col[j] = False
            if row[i] and col[j]:
                cnt += 1 
    print(cnt)
