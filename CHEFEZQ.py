for _ in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    temp = L.copy()
    for i in range(len(L)-1):
        if L[i] < K:
            print(i+1)
            break
        L[i+1] += L[i] - K 
    else:
        print((sum(temp) // K) + 1)
        
