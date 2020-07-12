for _ in range(int(input())):

    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    C = 0
    f = L[0]
    for i in L:
        C += abs(f - i)
    
    print(C)