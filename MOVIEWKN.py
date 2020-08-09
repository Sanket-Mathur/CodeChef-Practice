try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        R = list(map(int, input().split()))
        P = []
        for i in range(N):
            P.append(L[i] * R[i])
        if P.count(max(P)) == 1:
            print(P.index(max(P)) + 1)
        else:
            Rmax = [0] * N
            for i in range(N):
                if P[i] == max(P):
                    Rmax[i] = R[i]
            print(Rmax.index(max(Rmax)) + 1)
except:
    pass
