for _ in range(int(input())):
    X, Y = map(int, input().split())
    if X == Y:
        print(0)
    elif X < Y:
        if (Y-X) % 2 != 0:
            print(1)
        elif (Y-X) % 4 == 0:
            print(3)
        else:
            print(2)
    else:
        print(1 if (X-Y) % 2 == 0 else 2)
