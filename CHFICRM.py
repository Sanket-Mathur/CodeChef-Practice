for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    c_5 = c_10 = c_15 = 0 
    for i in L:
        if i == 5:
            c_5 += 1 
        elif i == 10:
            if c_5 > 0:
                c_5 -= 1 
                c_10 += 1
            else:
                print('NO')
                break
        else:
            if c_10 > 0:
                c_10 -= 1 
                c_15 += 1 
            elif c_5 > 1:
                c_5 -= 2
                c_15 += 1 
            else:
                print('NO')
                break
    else:
        print('YES')
