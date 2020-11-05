for _ in range(int(input())):
    S = list(input())
    Sa, Sb = map(int, input().split())
    A = S.index('A')
    B = S.index('B')
    flag = True
    while True:
        if A + Sa <= B:
            A += Sa 
        else:
            break
        if B + Sb >= A:
            B -= Sb 
        else:
            break
        if A == B:
            flag = False
            break
    print('safe' if flag else 'unsafe')
