try:
    for _ in range(int(input())):
        A, B = map(int, input().split())
        i = 1 
        while(True):
            if A >= i:
                A -= i 
                i += 1 
            else:
                print('Bob')
                break
            if B >= i:
                B -= i
                i += 1 
            else:
                print('Limak')
                break
except:
    pass
