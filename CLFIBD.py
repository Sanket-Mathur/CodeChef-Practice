for _ in range(int(input())):
    s = input()
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1 
        else:
            d[i] += 1 
    l = sorted(d.values())
    if len(l) < 3 or l[-1]==l[-2]+l[-3]:
        print('Dynamic')
    else:
        print('Not')
