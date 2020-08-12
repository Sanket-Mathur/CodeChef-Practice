try:
    for _ in range(int(input())):
        A = input()
        B = input()
        for i in set(A):
            if i in B:
                print('Yes')
                break
        else:
            print('No')
except:
    pass
