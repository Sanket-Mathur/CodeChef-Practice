for _ in range(int(input())):
    N, M, K, L, R = map(int, input().split())
    
    chosen = -1
    for i in range(N):
        c, p = map(int, input().split())
        
        if c < K and c+M < K:
            t = c+M
        elif c > K and c-M > K:
            t = c-M
        else:
            t = K
            
        if L <= t <= R and (p < chosen or chosen == -1):
            chosen = p 
            
    print(chosen)
