for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    new = {}
    for i in L:
        if i in new.keys():
            if i != list(new.keys())[-1]:
                print('NO')
                break
            new[i] += 1
        else:
            new[i] = 0
    else:
        print('YES' if len(new.values()) == len(set(new.values())) else 'NO')
