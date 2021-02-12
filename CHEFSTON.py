for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    profitMax = 0
    for i in range(N):
        pick = K // A[i]
        if pick * B[i] > profitMax:
            profitMax = pick * B[i]
    print(profitMax)
