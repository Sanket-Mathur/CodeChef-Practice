for _ in range(int(input())):
    S1 = input()
    S2 = input()
    b, o = [], []
    for i in range(3):
        if S1[i] == 'b' or S2[i] == 'b':
            b.append(i)
        if S1[i] == 'o' or S2[i] == 'o':
            o.append(i)
    if len(b) < 2 or not o:
        print('no')
    elif len(b) == 3:
        print('yes')
    else:
        possible = False
        for i in o:
            if i not in b: possible = True
        print('yes' if possible else 'no')
