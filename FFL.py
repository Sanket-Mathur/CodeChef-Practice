for _ in range(int(input())):
    N, K = map(int, input().split())
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))
    if 0 not in L2 or 1 not in L2:
        print('no')
    else:
        d, f = [], []
        for i in range(N):
            if L2[i] == 0:
                d.append(L1[i])
            else:
                f.append(L1[i])
        if K + min(d) + min(f) <= 100:
            print('yes')
        else:
            print('no')
