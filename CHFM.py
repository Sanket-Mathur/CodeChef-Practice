for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    mean = sum(L) / N 
    if mean not in L:
        print('Impossible')
    else:
        print(L.index(mean) + 1)
