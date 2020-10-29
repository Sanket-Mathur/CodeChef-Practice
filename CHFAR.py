for _ in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    ones = L.count(1)
    print('YES' if N-ones <= K else 'NO')
