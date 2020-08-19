try:
    S = list(input())
    c = h = e = f = 0
    for i in S:
        if i == 'C':
            c += 1
        elif i == 'H' and h < c:
            h += 1 
        elif i == 'E' and e < h:
            e += 1 
        elif i == 'F' and f < e:
            f += 1 
    print(f)
except:
    pass
