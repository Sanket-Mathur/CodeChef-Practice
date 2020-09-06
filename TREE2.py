for _ in range(int(input())):
    N = int(input())
    S = set(map(int, input().split()))
    if 0 in S:
        S.remove(0)
    print(len(S))
