try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        sign = []
        for l in L:
            sign.append(1 if l>=0 else 0)
        sub = [1]*N
        for i in range(N-2, -1, -1):
            if sign[i] != sign[i+1]:
                sub[i] = sub[i+1]+1
        print(*sub)
except:
    pass
