try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        m = min(L)
        print(m * (len(L) - 1))
except:
    pass
