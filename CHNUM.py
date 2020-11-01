for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    Gp = Gn = 0
    for i in A:
        if i < 0:
            Gn += 1 
        else:
            Gp += 1 
    if not Gn:
        print(Gp,Gp)
    elif not Gp:
        print(Gn, Gn)
    else:
        print(max(Gn,Gp), min(Gn,Gp))
