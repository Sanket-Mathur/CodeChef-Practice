try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        del L[0]
        x = 2
        while (x <= min(L)):
            C = 0
            for j in L:
                if j % x == 0:
                    C += 1 
            if C == len(L):
                for j in range(len(L)):
                    L[j] //= x 
                x = 2
            else:
                x += 1 
        print(*L)
except:
    pass
