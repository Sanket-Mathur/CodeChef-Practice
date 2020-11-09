for _ in range(int(input())):
    N = int(input())
    c = 1
    ctype = 1
    while True:
        if ctype == 1 and N > 2:
            ctype = 2
            N -= 2
        elif ctype == 2 and N > 8:
            ctype = 3
            N -= 8
        elif ctype == 3 and N > 16:
            ctype = 1 
            c *= 2
            N -= 16
        else:
            break
    if ctype == 1:
        print(c,0,0)
    elif ctype == 2:
        print(0,c,0)
    else:
        print(0,0,c)
