for _ in range(int(input())):
    L = ['']*3
    for i in range(3):
        L[i] = input()
    
    flag = False
    for i in range(2):
        for j in range(2):
            if L[i][j] == 'l' and L[i+1][j] == 'l' and L[i+1][j+1] == 'l':
                flag = True
                
    print('yes' if flag else 'no')
