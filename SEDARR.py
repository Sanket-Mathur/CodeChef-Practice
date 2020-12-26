for _ in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    if sum(L) % K == 0:
        print(0)
    else:
        print(1)
