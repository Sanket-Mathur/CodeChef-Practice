for _ in range(int(input())):
    N = int(input())
    L = []
    for n in range(N):
        l = list(map(int, input().split()))
        L.append(l)
    c = 0
    i = 0 
    direct = 0 if L[0][1] == 2 else 1 
    while i < N-1:
        i += 1 
        if (direct == 0 and L[0][i] == i+1) or (direct == 1 and L[i][0] == i+1):
            continue
        direct = 0 if direct else 1 
        c += 1
    if direct:
        c += 1
    print(c)
