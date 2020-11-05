for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    typ = dishes = -1
    for i in sorted(set(L)):
        index = c = 0
        while index < N:
            if L[index] == i:
                c += 1
                index += 1
            index += 1
        if c > dishes or dishes == -1:
            typ = i 
            dishes = c 
    print(typ)
