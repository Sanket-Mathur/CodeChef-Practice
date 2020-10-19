for _ in range(int(input())):
    S = int(input())
    loss = 0
    for i in range(S):
        P, Q, X = map(int, input().split())
        Orig = P
        P = P + P*X/100
        loss += (Orig - (P - P*X/100)) * Q
    print(loss)
