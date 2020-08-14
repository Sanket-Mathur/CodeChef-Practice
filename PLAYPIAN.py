try:
    for _ in range(int(input())):
        L = input()
        for i in range(0, len(L), 2):
            if L[i] == L[i+1]:
                print('no')
                break
        else:
            print('yes')
except:
    pass
