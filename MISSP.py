try:
    for _ in range(int(input())):
        N = int(input())
        L = []
        for i in range(N):
            x = int(input())
            if x in L:
                L.remove(x)
            else:
                L.append(x)
        print(*L)
except:
    pass
