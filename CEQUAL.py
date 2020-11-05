for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    if len(L) == len(set(L)):
        print('No')
    else:
        print('Yes')
