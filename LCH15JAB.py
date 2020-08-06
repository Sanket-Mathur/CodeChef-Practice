try:
    for _ in range(int(input())):
        S = input()
        l = []
        for i in set(S):
            l.append(S.count(i))
        m = max(l)
        l.remove(m)
        if m == sum(l):
            print('YES')
        else:
            print('NO')
except:
    pass
