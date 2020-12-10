for _ in range(int(input())):
    N, M = map(int, input().split())
    X, Y, S = map(int, input().split())
    XL = list(map(int, input().split())) if X > 0 else []
    YL = list(map(int, input().split())) if Y > 0 else []
    availX, availY = 0, 0
        
    curr = 0
    for i in XL:
        availX += (i - curr - 1) // S
        curr = i
    availX += (N - curr) // S
    
    curr = 0
    for i in YL:
        availY += (i - curr - 1) // S 
        curr = i
    availY += (M - curr) // S
    
    print(availX * availY)
