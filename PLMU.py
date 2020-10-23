for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    c0 = c2 = 0
    for i in L:
        if i == 0:
            c0 += 1 
        elif i == 2:
            c2 += 1 
    print(c0*(c0-1)//2 + c2*(c2-1)//2)
