for _ in range(int(input())):

    N = int(input())

    L = list(map(int, input().split()))

    D = 0
    for i in range(N-1):
        D += abs(L[i] - L[i+1]) - 1

    print(D)