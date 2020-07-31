try:
    S, A, B = [], [], []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        A.append(a); B.append(b)
        a = sum(A); b = sum(B)
        S.append(a-b)
    if max(S) > abs(min(S)):
        print(1, max(S))
    else:
        print(2, abs(min(S)))
except:
    pass
