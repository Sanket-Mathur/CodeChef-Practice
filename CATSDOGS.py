try:
    for _ in range(int(input())):
        C, D, L = map(int, input().split())
        maxL = C*4 + D*4
        minL = D*4 + (0 if D*2 >= C else (C - D*2) * 4)
        if minL <= L <= maxL and L % 4 == 0:
            print('yes')
        else:
            print('no')
except:
    pass
