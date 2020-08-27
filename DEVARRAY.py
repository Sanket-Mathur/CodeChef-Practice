try:
    N, Q = map(int, input().split())
    L = list(map(int, input().split()))
    MIN, MAX = min(L), max(L)
    while Q > 0:
        Q -= 1
        q = int(input())
        if MIN <= q <= MAX:
            print('Yes')
        else:
            print('No')
except:
    pass
