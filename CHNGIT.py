try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        count = 0
        for i in set(L):
            if count < L.count(i):
                count = L.count(i)
        print(len(L)-count)
except:
    pass
