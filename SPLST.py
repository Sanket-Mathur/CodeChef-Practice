for _ in range(int(input())):
    a,b,c,x,y = map(int, input().split())
    L = [a,b,c]
    possible = 0
    for i in range(2):
        for j in range(i+1,3):
            if L[i] <= x and L[j] <= y:
                possible += 1 
            if L[i] <= y and L[j] <= x:
                possible += 1 
    if possible and (sum(L) == x+y):
        print('YES')
    else:
        print('NO')
