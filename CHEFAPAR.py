for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    
    late = False
    lN = 0
    for i in L:
        if i == 0: late = True
        if late: lN += 1 
    
    print(L.count(0)*1000 + lN*100)
