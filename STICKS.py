try:
    for _ in range(int(input())):
        N = int(input())
        L = sorted(map(int, input().split()), reverse=True)
        l = b = -1
        i = 0
        while (l == -1 or b == -1) and i < N-1:
            if L[i] == L[i+1]:
                b = l 
                l = L[i]
                i += 2
            else:
                i += 1 
        if l == -1 or b == -1:
            print(-1)
        else:
            print(l*b)
except:
    pass
