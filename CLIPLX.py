try:
    for _ in range(int(input())):
        X, Y = map(int, input().split())
        print(0 if X <= Y else X-Y)
except:
    pass
