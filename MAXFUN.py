for _ in range(int(input())):
    N = int(input())
    S = set(map(int, input().split()))
    if len(S) == 1:
        print(0)
    else:
        print(2 * (max(S) - min(S)))
