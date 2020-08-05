try:
    for _ in range(int(input())):
        M, x, y = map(int, input().split())
        
        H = list(map(int, input().split()))
        H.sort()

        R = x*y 
        C = 0 
        
        if H[0] - 1 > R:
            C += H[0] - 1 - R 
        
        for i in range(1, len(H)):
            if H[i] - H[i-1] > 2*R:  
                C += H[i] - H[i-1] - 2*R - 1
        
        if 100 - H[-1] > R:
            C += 100 - H[-1] - R 
        
        print(C)
        
except:
    pass
