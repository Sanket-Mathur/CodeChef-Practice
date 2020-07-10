for _ in range(int(input())):

    A, B = 0, 0
    for N in range(int(input())):

        x, y = map(int, input().split())
        x = [int(i) for i in list(str(x))]
        y = [int(i) for i in list(str(y))]

        if sum(x) >= sum(y):
            A += 1

        if sum(x) <= sum(y):
            B += 1
    
    if A > B:
        print('0', A)
    elif B > A:
        print('1', B)
    else:
        print('2', A)