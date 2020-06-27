for T in range(int(input())):

    N = int(input())
    B = list(map(int, input().split()))

    if (100 <= sum(B) < 100+N-B.count(0)):
        print('YES')
    else:
        print('NO')