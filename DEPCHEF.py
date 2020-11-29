for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    while True:
        m = d.index(max(d))
        if not d[m]:
            print(-1)
            break
        elif d[m] > a[m-1] + a[(m+1) % N]:
            print(d[m])
            break
        else:
            d[m] = 0
        
