for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    
    L_copy = L.copy()
    N1 = max(L_copy)
    L_copy.remove(N1)
    N2 = max(L_copy)
    
    req_out = 0
    for i in range(N):
        for j in range(N):
            if i != j and ((L[i]==N1 and L[j]==N2) or (L[i]==N2 and L[j]==N1)):
                req_out += 1
    
    tot_out = N * (N-1) / 2
    
    print(req_out / (2 * tot_out))
