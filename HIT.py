for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()), reverse=True)
    
    cut = []
    flag = True
    for i in range(4):
        a = set(L[:N//4])
        cut.append(min(list(a)))
        L = L[N//4:]
        for i in a:
            if i in L:
                flag = False
        if not flag:
            break

    if flag:
        print(*cut[2::-1])
    else:
        print(-1)

