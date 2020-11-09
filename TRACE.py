for _ in range(int(input())):
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        
    sums = []
    for x in range(N):
        i = 0
        j = x
        c = 0
        while i < N and j < N:
            c += L[i][j]
            i += 1 
            j += 1 
        sums.append(c)
        i = x
        j = 0
        c = 0
        while i < N and j < N:
            c += L[i][j]
            i += 1 
            j += 1 
        sums.append(c)
    
    print(max(sums))
