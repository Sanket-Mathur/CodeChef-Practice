try:
    for _ in range(int(input())):
        exp = input()
        ans = []
        oper = []
        for i in list(exp):
            if i.isalpha():
                ans.append(i)
            elif i == ')':
                x = oper.pop(len(oper)-1)
                while(x != '('):
                    ans.append(x)
                    x = oper.pop(len(oper)-1)
            else:
                oper.append(i)
        print(*ans, sep='')
except:
    pass
