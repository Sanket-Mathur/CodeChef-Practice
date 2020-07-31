try:
    for i in range(int(input())):
        S = input()
        if len(S) % 2 == 0:
            A = S[ :len(S)//2]
            B = S[len(S)//2: ]
        else:
            A = S[ :len(S)//2]
            B = S[len(S)//2+1: ]
        if sorted(list(A)) == sorted(list(B)):
            print('YES')
        else:
            print('NO')
except:
    pass
