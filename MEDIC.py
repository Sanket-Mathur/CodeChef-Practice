for _ in range(int(input())):
    y, m, d = map(int, input().split(':'))
    if m in [1,3,5,7,8,10,12]:
        print((31 - d) // 2 + 1)
    elif m in [4,6,9,11]:
        print((61 - d) // 2 + 1)
    else:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            print((29 - d) // 2 + 1)
        else:
            print((59 - d) // 2 + 1)
