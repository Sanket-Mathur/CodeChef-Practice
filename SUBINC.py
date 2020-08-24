try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        c = [0] * N
        c[0] = 1
        for i in range(1,N):
            if L[i-1] <= L[i]:
                c[i] = c[i-1] + 1
            else:
                c[i] = 1
        print(sum(c))
except:
    pass
