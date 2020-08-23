try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        L = list(map(int, input().split()))
        flag = True
        w = trips = 0
        while L:
            if L[0] > K:
                flag = False
                break
            if w == 0:
                trips += 1 
                w += L[0]
                del L[0]
            elif w + L[0] <= K:
                w += L[0]
                del L[0]
            else:
                w = L[0]
                trips += 1 
                del L[0]
        if flag:
            print(trips)
        else:
            print(-1)
except:
    pass
