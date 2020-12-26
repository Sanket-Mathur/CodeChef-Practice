def check(A, R, C):
    x = C-2
    while x > 0:
        i,j = x,0
        curr = A[i][j]
        while i < R and j < C:
            if A[i][j] != curr:
                return False
            i += 1 
            j += 1 
        x -= 1
    x = 0
    while x < R:
        i,j = 0,x
        curr = A[i][j]
        while i < R and j < C:
            if A[i][j] != curr:
                return False
            i += 1 
            j += 1 
        x += 1
    return True

for _ in range(int(input())):
    R, C = map(int, input().split())
    L = []
    for i in range(R):
        L.append(list(map(int, input().split())))
    good = check(L, R, C)
    for q in range(int(input())):
        X, Y, V = map(int, input().split())
        L[X-1][Y-1] = V 
        if not good:
            good = check(L, R, C)
        else:
            if (X > 1 and Y > 1) and (L[X-1][Y-1] != L[X-2][Y-2]):
                good = False
            elif (X < R and Y < C) and (L[X-1][Y-1] != L[X][Y]):
                good = False
        print('Yes' if good else 'No')
