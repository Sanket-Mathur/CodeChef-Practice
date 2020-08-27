try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        while len(L) > 2:
            l = L[:3]
            l.remove(min(l))
            L.remove(min(l))
        print(*L)
except:
    pass
