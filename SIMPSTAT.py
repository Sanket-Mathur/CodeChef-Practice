try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        L = sorted(map(int, input().split()))
        L = L[K : len(L)-K]
        print("%.6f" % (sum(L) / len(L)))
except:
    pass
