try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        L.sort()
        print(L[0]+L[1])
except:
    pass
