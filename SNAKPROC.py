try:
    for _ in range(int(input())):
        N = int(input())
        S = list(input())
        curr = wrong = False
        for i in S:
            if i == 'H':
                if curr:
                    wrong = True
                    break
                else:
                    curr = True
            elif i == 'T':
                if curr:
                    curr = False
                else:
                    wrong = True
                    break
        print('Invalid' if wrong or curr else 'Valid')
            
except:
    pass
