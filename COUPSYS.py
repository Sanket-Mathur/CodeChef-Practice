def check(d):
    c = x = -1
    for i in d.keys():
        if d[i] > x:
            x = d[i]
            c = i 
        elif d[i] == x and i < c:
            c = i 
    return x, c

for _ in range(int(input())):
    l1, l2, l3 = {}, {}, {}
    for i in range(int(input())):
        c, l, x = map(int, input().split())
        if l == 1:
            if c in l1.keys():
                l1[c] = max(l1[c], x)
            else:
                l1[c] = x 
        elif l == 2:
            if c in l2.keys():
                l2[c] = max(l2[c], x)
            else:
                l2[c] = x 
        else:
            if c in l3.keys():
                l3[c] = max(l3[c], x)
            else:
                l3[c] = x
    print(*check(l1))
    print(*check(l2))
    print(*check(l3))
