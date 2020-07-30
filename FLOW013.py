try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        if sum(L)==180:
            print('YES')
        else:
            print('NO')
except:
    pass
