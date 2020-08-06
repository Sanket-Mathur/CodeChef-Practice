try:
    for _ in range(int(input())):
        N = int(input())
        L1 = list(map(int, input().split()))
        L2 = list(map(int, input().split()))
        for i in range(len(L1)-1,0,-1):
            L1[i] = L1[i] - L1[i-1]
        C = 0
        for i in range(len(L1)):
            if L1[i] >= L2[i]:
                C += 1 
        print(C)
except:
    pass
