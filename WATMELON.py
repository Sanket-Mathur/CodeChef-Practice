for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    print('YES' if sum(L) >= 0 else 'NO')
