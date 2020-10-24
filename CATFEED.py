for _ in range(int(input())):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    for i in range(0,M,N):
        l = L[i:i+N]
        if len(l) != len(set(l)):
            print('NO')
            break
    else:
        print('YES')
