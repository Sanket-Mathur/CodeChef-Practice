try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        if 2 in L or 5 not in L or sum(L)/N < 4.0:
            print('No')
        else:
            print('Yes')
except:
    pass
