for _ in range(int(input())):
    X, Y, N = map(int, input().split())
    if X == Y:
        print(0)
    else:
        c = 0
        for Z in range(N+1):
            if X^Z < Y^Z:
                c += 1 
        print(c)
