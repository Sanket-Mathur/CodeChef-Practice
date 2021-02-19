for _ in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    currX = currY = 0
    cnt = 0
    for i in range(N):
        preX, preY = currX, currY
        currX += X[i]
        currY += Y[i]
        if preX == preY and currX == currY:
            cnt += X[i]
    print(cnt)
