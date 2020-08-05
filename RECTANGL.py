try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        for i in L:
            if L.count(i) < 2:
                print("NO")
                break
        else:
            print("YES")
except:
    pass
