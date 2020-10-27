for _ in range(int(input())):
    N, U, D = map(int, input().split())
    L = list(map(int, input().split()))
    c = 0
    para = True
    while c < N-1:
        if L[c] <= L[c+1] and L[c+1]-L[c]<=U:
            c += 1 
        elif L[c] > L[c+1] and L[c]-L[c+1]<=D:
            c += 1 
        elif L[c] > L[c+1] and para:
            c += 1 
            para = False
        else:
            break
    print(c+1)
