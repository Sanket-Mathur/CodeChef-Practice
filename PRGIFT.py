try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        L = list(map(int, input().split()))
        c = 0
        for i in L:
            if not i % 2:
                c += 1
        if c == N and K == 0:
            print('NO')
        else:
            if c >= K:
                print('YES')
            else:
                print('NO')
except:
    pass
