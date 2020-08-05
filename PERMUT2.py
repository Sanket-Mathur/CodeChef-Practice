try:
    T = int(input())
    while(T):
        L = list(map(int, input().split()))
        A = [None] * T
        for i in range(T):
            A[L[i] - 1] = i + 1
        if A == L:
            print('ambiguous')
        else:
            print('not ambiguous')
        T = int(input())
except:
    pass
