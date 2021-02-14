for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    m = min(L)
    L.remove(m)
    dist = 0
    for i in L:
        dist += (m * i)
    print(dist)
