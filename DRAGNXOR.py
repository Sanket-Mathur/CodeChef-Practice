for _ in range(int(input())):
    N, A, B = map(int, input().split())
    cA = bin(A).count('1')
    cB = bin(B).count('1')
    res = ('1' * (N - abs(cA + cB - N))) + ('0' * abs(cA + cB - N))
    print(int(res, 2))
