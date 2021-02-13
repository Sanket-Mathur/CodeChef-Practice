for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    print(L.index(min(L)) + 1)
