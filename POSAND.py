for _ in range(int(input())):
    
    N = int(input())
    
    if N == 1:
        print(1)
    elif N & N-1 == 0:
        print(-1)
    else:
        L = list(range(1,N+1))
        L[:3] = [2,3,1]
        for i in range(3,N):
            if L[i] & L[i-1] == 0:
                L[i] , L[i+1] = L[i+1], L[i]
        print(*L)
