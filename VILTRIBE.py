for _ in range(int(input())):
    T = list(input())
    A = B = 0
    curr = ''
    empty = 0
    for i in T:
        if i == 'A':
            if curr == 'A':
                A += empty
            curr = 'A'
            A += 1 
            empty = 0
        elif i == 'B':
            if curr == 'B':
                B += empty
            curr = 'B'
            B += 1 
            empty = 0
        else:
            empty += 1
    print(A,B)
