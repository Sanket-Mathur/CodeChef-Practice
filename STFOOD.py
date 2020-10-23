for _ in range(int(input())):
    N = int(input())
    C = []
    for i in range(N):
        S, P, V = map(int, input().split())
        if S < P:
            C.append((P // (S+1)) * V)
    print(max(C) if C else 0)
