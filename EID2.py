for _ in range(int(input())):
    L = list(map(int, input().split()))
    A, C = L[:3], L[3:]
    X = sorted(zip(A,C))
    flag = True
    for i in range(2):
        if X[i][0] < X[i+1][0] and X[i][1] >= X[i+1][1]:
            flag = False
        elif X[i][0] == X[i+1][0] and X[i][1] != X[i+1][1]:
            flag = False
    print('FAIR' if flag else 'NOT FAIR')
