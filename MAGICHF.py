for _ in range(int(input())):
    N, X, S = map(int, input().split())
    curr = X 
    for i in range(S):
        L = list(map(int, input().split()))
        if L[0] == curr:
            curr = L[1]
        elif L[1] == curr:
            curr = L[0]
    print(curr)
