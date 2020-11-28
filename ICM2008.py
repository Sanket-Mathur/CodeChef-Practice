for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if c==d:
        if a==b:
            print('YES')
        else:
            print('NO')
    elif abs(a-b) % abs(c-d) == 0:
        print('YES')
    else:
        print('NO')
