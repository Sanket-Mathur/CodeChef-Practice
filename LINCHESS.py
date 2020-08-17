try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        P = list(map(int, input().split()))
        L1 = []; L2 = []
        for i in P:
            if K % i == 0:
                L1.append(K // i)
                L2.append(i)
        if L1 != []:
            print(L2[L1.index(min(L1))])
        else:
            print(-1)
except:
    pass
