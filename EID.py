for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    min_diff = max(L)
    for i in range(N-1):
        if abs(L[i] - L[i+1]) < min_diff:
            min_diff = abs(L[i] - L[i+1])
    print(min_diff)
