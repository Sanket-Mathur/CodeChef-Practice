try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        L = list(map(int, input().split()))
        if K == 1:
            if sum(L) % 2:
                print('even')
            else:
                print('odd')
        else:
            print('even')
except:
    pass
