try:
    
    def F(S):
        balance = 0
        max_balance = 0
        for i in S:
            if i == '(':
                balance += 1 
            elif i == ')':
                balance -= 1 
            max_balance = max(balance, max_balance)
        return max_balance
    
    for _ in range(int(input())):
        S = input()
        max_balance = F(S)
        for i in range(max_balance):
            print('(', end='')
        for i in range(max_balance):
            print(')', end='')
        print('')
    
except:
    pass
