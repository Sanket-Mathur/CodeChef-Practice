for _ in range(int(input())):
    N, K = map(int, input().split())
    L = sorted(map(int, input().split()), reverse=True)
    cut = L[K-1]
    c = K
    for i in range(K, N):
        if L[i] == cut:
            c += 1 
        else:
            break
    print(c)
