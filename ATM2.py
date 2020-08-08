try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        L = list(map(int, input().split()))
        for i in L:
            if i <= K:
                print('1', end='')
                K -= i
            else:
                print('0', end='')
        print('')
except:
    pass
