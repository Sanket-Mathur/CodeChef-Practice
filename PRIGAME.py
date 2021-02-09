def Prime(n):
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return 0
for _ in range(int(input())):
    X, Y = map(int, input().split())
    divisible = 0
    for i in range(1, X+1):
        if Prime(i) == 0:
            divisible += 1 
    print('Divyam' if divisible > Y else 'Chef')
