for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    s = 0
    for i in range(N // 2):
        s += abs(L[i] - L[N-i-1])
    print(s)
