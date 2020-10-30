for _ in range(int(input())):
    L = []
    for i in range(3):
        L.append(list(map(int, input().split())))
    L.sort()
    flag = True
    for i in range(1,3):
        if not ((L[i-1][0]<L[i][0] or L[i-1][1]<L[i][1] or L[i-1][2]<L[i][2]) and (L[i-1][0]<=L[i][0] and L[i-1][1]<=L[i][1] and L[i-1][2]<=L[i][2])):
            flag = False
    print('yes' if flag else 'no')
