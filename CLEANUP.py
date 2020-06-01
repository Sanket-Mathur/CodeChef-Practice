for t in range(int(input())):

    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    j = [x+1 for x in range(n)]

    for i in A:
        if i in j:
            j.remove(i)
    
    c, a = 0, 1
    while(c < len(j)):
        print(j[c], end=' ')
        c += 2
    print(' ')
    while(a < len(j)):
        print(j[a], end=' ')
        a += 2
    print(' ')