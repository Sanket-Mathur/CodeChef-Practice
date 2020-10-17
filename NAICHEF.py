for _ in range(int(input())):
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))
    fav1 = X.count(A)
    fav2 = X.count(B)
    print(fav1/N * fav2/N)
