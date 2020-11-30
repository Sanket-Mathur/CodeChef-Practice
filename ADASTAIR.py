for _ in range(int(input())):
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    h.insert(0,0)
    c = 0
    for i in range(1, N+1):
        c += (h[i] - h[i-1] - 1) // K
    print(c)
