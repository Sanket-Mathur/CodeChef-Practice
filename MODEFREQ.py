for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    first = [L.count(i) for i in set(L)]
    second = [first.count(i) for i in set(first)]
    maxr = max(second)
    res = [i for i in set(first) if first.count(i) == maxr]
    print(min(res))
