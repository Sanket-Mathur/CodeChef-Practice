try:
    for _ in range(int(input())):
        N = int(input())
        S = input()
        if 'I' in S:
            print('INDIAN')
        elif 'Y' in S:
            print('NOT INDIAN')
        else:
            print('NOT SURE')
except:
    pass
