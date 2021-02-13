for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    maxDiff = 0
    pre = L[0]
    for i in range(1,len(L)):
        diff = L[i] - pre
        if diff > 0:
            if diff > maxDiff:
                maxDiff = diff 
        else:
            pre = L[i]
    print('UNFIT' if maxDiff == 0 else maxDiff)
