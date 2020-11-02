for _ in range(int(input())):
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, list(input()))))
    c = 0
    for i in range(len(L[0])):
        x = L[0][i]
        for j in range(1, N):
            x ^= L[j][i]
        if x:
            c += 1 
    print(c)
