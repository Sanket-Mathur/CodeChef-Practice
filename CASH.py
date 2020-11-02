for _ in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    c = 0
    for i in L:
        c += i % K 
    print(c % K)
