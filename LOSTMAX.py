try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        L.remove(len(L)-1)
        print(max(L))
except:
    pass
