try:
    for _ in range(int(input())):
        N = int(input())
        L1 = input()
        L2 = input()
        S = list(map(int, input().split()))
        if L1==L2:
            print(S[-1])
        else:
            c = 0
            for i in range(N):
                if L1[i] == L2[i]:
                    c += 1
            print(max(S[:c+1]))
except:
    pass
