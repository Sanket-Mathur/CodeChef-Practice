for _ in range(int(input())):
    N, A, B, C, D, P, Q, Y = map(int, input().split())
    X = list(map(int, input().split()))
    X.insert(0,0)
    train = None
    if abs(X[A] - X[C]) * P <= Y:
        wait = Y - abs(X[A] - X[C]) * P
        train = (abs(X[A] - X[C]) * P) + (abs(X[D] - X[C]) * Q) + (abs(X[B] - X[D]) * P) + wait
    walk = abs(X[B] - X[A]) * P 
    if train:
        print(min(walk, train))
    else:
        print(walk)
