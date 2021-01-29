def solve(N,x,y,k):
    if x == y:
        return (N,N)
    elif x > y:
        y += N - x 
        x = N 
        if k % 4 == 1:
            return (x,y) 
        x = y  
        y = N 
        if k % 4 == 2:
            return (x,y)  
        y -= x 
        x = 0
        if k % 4 == 3:
            return (x,y)  
        return (x+y, 0)
    else:
        x += N - y  
        y = N 
        if k % 4 == 1:
            return (x,y)  
        y = x 
        x = N 
        if k % 4 == 2:
            return (x,y)  
        x -= y  
        y = 0
        if k % 4 == 3:
            return (x,y)  
        return (0, x+y)
    
for _ in range(int(input())):
    N, K, x, y = map(int, input().split())
    print(*solve(N,x,y,K))
