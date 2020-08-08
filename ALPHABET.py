try:
    S = list(input())
    for _ in range(int(input())):
        X = list(input())
        flag = True
        for i in X:
            if i not in S:
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
except:
    pass
