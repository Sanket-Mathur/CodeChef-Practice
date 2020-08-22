try:
    for _ in range(int(input())):
        X, Y, Z = map(int, input().split())
        if X+Y==Z or Y+Z==X or Z+X==Y:
            print('yes')
        else:
            print('no')
except:
    pass
