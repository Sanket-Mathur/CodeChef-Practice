try:
    for _ in range(int(input())):
        N = int(input())
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        X1 = [X[i] for i in range(N) if not i%2]
        Y1 = [Y[i] for i in range(N) if i%2]
        X2 = [X[i] for i in range(N) if i%2]
        Y2 = [Y[i] for i in range(N) if not i%2]
        print(min(sum(X1)+sum(Y1), sum(X2)+sum(Y2)))
except:
    pass
