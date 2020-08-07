try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        L = list(map(int, input().split()))
        c = 0
        for i in L:
            if (i+K) % 7 == 0:
                c += 1
        print(c)
except:
    pass
