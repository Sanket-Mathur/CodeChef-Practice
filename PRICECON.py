for _ in range(int(input())):
    N, K = map(int, input().split())
    c = 0
    for i in list(map(int, input().split())):
        if i > K:
            c += i - K
    print(c)
