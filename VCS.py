try:
    for _ in range(int(input())):
        N, M, K = map(int, input().split())
        L1 = list(map(int, input().split()))
        L2 = list(map(int, input().split()))
        c1 = c2 = 0
        for n in range(1,N+1):
            if n in L1 and n in L2:
                c1 += 1 
            elif n not in L1 and n not in L2:
                c2 += 1 
        print(c1, c2)
except:
    pass
