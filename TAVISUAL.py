for _ in range(int(input())):
    N, C, Q = map(int, input().split())
    for q in range(Q):
        L, R = map(int, input().split())
        if L <= C <= R:
            C = L + R - C 
    print(C)
