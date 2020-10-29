for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
        
    count = 0
    for i in range(a,b+1):
        if i < c and i < d:
            count += d - c + 1
        elif i < d:
            count += d - i

    print(count)
