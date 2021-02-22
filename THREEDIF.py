for _ in range(int(input())):
    L = sorted(map(int, input().split()))
    print((L[0] * (L[1]-1) * (L[2]-2)) % (10**9 + 7))
