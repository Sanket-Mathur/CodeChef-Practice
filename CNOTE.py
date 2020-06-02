for t in range(int(input())):

    X, Y, K, N = map(int, input().split())
    P = []
    C = []
    for i in range(N):
        p, c = map(int, input().split())
        P.append(p)
        C.append(c)

    req = X-Y
    if(max(P) < req):
        print('UnluckyChef')
    else:
        flag = 0
        for i in range(len(P)):
            if P[i] >= req and C[i] <= K:
                print('LuckyChef')
                flag = 1
                break
        if(flag == 0):
            print('UnluckyChef')