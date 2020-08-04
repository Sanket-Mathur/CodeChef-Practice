try:
    K, N = map(int, input().split())
    L = [0]*K
    for i in range(N):
        a = input()
        if a == 'CLOSEALL':
            L = [0]*K
        elif a == 'OPENALL':
            L = [1]*K
        else:
            n = int(a.split(' ')[1])
            if L[n-1] == 1:
                L[n-1] = 0
            else:
                L[n-1] = 1
        print(L.count(1))
except:
    pass
