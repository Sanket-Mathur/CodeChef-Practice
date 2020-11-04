for _ in range(int(input())):
    N, M = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    flag = True
    for i in range(N):
        for j in range(M):
            k = 0
            if i-1 >= 0:
                k += 1
            if i+1 < N:
                k += 1 
            if j-1 >= 0:
                k += 1 
            if j+1 < M:
                k += 1 
            if k <= L[i][j]:
                flag = False
                break
        if not flag:
            break
    print('Stable' if flag else 'Unstable')
