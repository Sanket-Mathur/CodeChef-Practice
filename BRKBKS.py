for _ in range(int(input())):
    L = list(map(int, input().split()))
    S = L[0]
    W = L[1:]
    c = 0
    if W[0] + W[1] <= S:
        if W[0] + W[1] + W[2] <= S:
            print(1)
        else:
            print(2)
    elif W[2] + W[1] <= S:
        print(2)
    else:
        print(3)
