try:
    for _ in  range(int(input())):
        N, K = map(int, input().split())
        L = []
        for i in range(1,K+1):
            L.append(N % i)
        print(max(L))
except:
    pass
