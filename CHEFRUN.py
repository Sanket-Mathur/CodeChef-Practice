try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        S1, S2 = abs(L[2]-L[0])/L[3], abs(L[2]-L[1])/L[4]
        if S1 < S2:
            print('Chef')
        elif S1 > S2:
            print('Kefa')
        else:
            print('Draw')
except:
    pass
