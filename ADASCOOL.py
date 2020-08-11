try:
    for _ in range(int(input())):
        N, M = map(int, input().split())
        if N%2==0 or M%2==0:
            print('YES')
        else:
            print('NO')
except:
    pass
