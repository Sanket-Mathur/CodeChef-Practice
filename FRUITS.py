try:
    for _ in range(int(input())):
        N, M, K = map(int, input().split())
        diff = abs(N-M)
        print(0 if diff <= K else diff-K)
except:
    pass
