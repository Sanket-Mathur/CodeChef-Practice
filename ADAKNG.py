for _ in range(int(input())):
    Y, X, K = map(int, input().split())
    l = X - K if X-K > 0 else 1 
    r = X + K if X+K < 9 else 8 
    u = Y - K if Y-K > 0 else 1 
    d = Y + K if Y+K < 9 else 8 
    print((r-l+1) * (d-u+1))
