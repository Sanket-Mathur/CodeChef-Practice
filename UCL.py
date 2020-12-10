for _ in range(int(input())):
    d = {}
    for i in range(12):
        t1, s1, vs, s2, t2 = input().split()
        s1 = int(s1)
        s2 = int(s2)
        
        if t1 not in d:
            d[t1] = [0,0]
        if t2 not in d:
            d[t2] = [0,0]
            
        if s1 > s2:
            d[t1][0] += 3
        elif s2 > s1:
            d[t2][0] += 3
        else:
            d[t1][0] += 1 
            d[t2][0] += 1 
        
        d[t1][1] += s1-s2
        d[t2][1] += s2-s1
        
    d = sorted(d, key=d.get, reverse=True)
    print(d[0], d[1])
