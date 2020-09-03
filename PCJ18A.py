for _ in range(int(input())):
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    for i in L:
        if i >= X:
            print('YES')
            break
    else:
        print('NO')
