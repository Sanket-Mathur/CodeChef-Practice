for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    if len(set(L)) != N:
        print('no')
    elif L == list(range(1,N+1)):
        print('no')
    else:
        for i in range(1,N+1):
            if i not in L:
                print('no')
                break
        else:
            print('yes')
