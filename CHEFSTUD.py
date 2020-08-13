try:
    for _ in range(int(input())):
        S = list(input())
        for i in range(len(S)):
            if S[i] == '<':
                S[i] = '>'
            elif S[i] == '>':
                S[i] = '<'
        c = (''.join(S)).count('><')
        print(c)
except:
    pass
