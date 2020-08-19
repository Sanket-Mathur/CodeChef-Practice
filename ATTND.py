try:
    for _ in range(int(input())):
        F, L = [], []
        for n in range(int(input())):
            x = input().split()
            F.append(x[0])
            L.append(x[1])
        for i in range(len(F)):
            if F.count(F[i]) == 1:
                print(F[i])
            else:
                print(F[i], L[i])
except:
    pass
