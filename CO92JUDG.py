try:
    for _ in range(int(input())):
        N = int(input())
        L1 = list(map(int, input().split()))
        L2 = list(map(int, input().split()))
        a = sum(L1) - max(L1)
        b = sum(L2) - max(L2)
        if a == b:
            print('Draw')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
except:
    pass
