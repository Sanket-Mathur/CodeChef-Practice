try:
    for _ in range(int(input())):
    
        N, K = map(int, input().split())
        S = list(map(int, input().split()))
    
        L = []
        for i in S:
            if i % K == 0:
                L.append(1)
            else:
                L.append(0)
    
        print(*L, sep='')
    
except:
    pass
