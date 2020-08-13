try:
    for _ in range(int(input())):
        L = list(input())
        a = b = 0
        for i in L:
            if i == '1':
                a += 1 
            else:
                b += 1 
        if (a > b):
            print('WIN')
        else:
            print('LOSE')
except:
    pass
