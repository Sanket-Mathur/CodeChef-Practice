for _ in range(int(input())):
    S = input()
    ch = ord(S[0])
    oper = 1 
    for i in S:
        if ord(i) == ch:
            oper += 1 
        elif ord(i) > ch:
            oper += ord(i) - ch + 1
            ch = ord(i)
        else:
            oper += 27 - ch + ord(i)
            ch = ord(i)
    print('YES' if oper <= 11 * len(S) else 'NO')
