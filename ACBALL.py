for _ in range(int(input())):
    X = input()
    Y = input()
    Z = []
    for i in range(len(X)):
        if X[i] == Y[i] and X[i] == 'B':
            Z.append('W')
        else:
            Z.append('B')
    print(''.join(Z))
