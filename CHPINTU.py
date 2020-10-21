for _ in range(int(input())):
    N, M = map(int, input().split())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))
    F_s = list(set(F))
    TP = []
    for i in range(len(F_s)):
        c = 0
        for j in range(N):
            if F_s[i] == F[j]:
                c += P[j]
        TP.append(c)
    print(min(TP))
