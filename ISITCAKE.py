for _ in range(int(input())):
    c = 0
    for i in range(10):
        x = list(map(int, input().split()))
        for j in range(10):
            if x[j] <= 30:
                c += 1 
    print('yes' if c >= 60 else 'no')
