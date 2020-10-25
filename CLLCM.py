for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    for i in L:
        if not i % 2:
            print('NO')
            break
    else:
        print('YES')
