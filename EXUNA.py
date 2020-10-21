for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    mod = L[0]
    for i in range(1,N):
        mod = mod % L[i]
    print(mod)
