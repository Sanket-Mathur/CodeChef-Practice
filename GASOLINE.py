for _ in range(int(input())):
    N = int(input())
    f = list(map(int, input().split()))
    c = list(map(int, input().split()))
    traveled = total = 0
    f = list(list(zip(*(sorted(zip(c,f)))))[1])
    c.sort()
    i = 0
    while traveled < N:
        traveled += f[i]
        total += f[i] * c[i]
        i += 1
    if traveled > N:
        total -= (traveled-N)*c[i-1]
    print(total)
