for _ in range(int(input())):
    N, M = map(int, input().split())
    c1, c2 = 0, 0
    for i in range(N):
        l = input()
        for j in range(M):
            if i%2==0 and j%2==0 and l[j]=='G':
                c1 += 3
            elif i%2==0 and j%2!=0 and l[j]=='R':
                c1 += 5
            elif i%2!=0 and j%2==0 and l[j]=='R':
                c1 += 5
            elif i%2!=0 and j%2!=0 and l[j]=='G':
                c1 += 3
        for j in range(M):
            if i%2==0 and j%2==0 and l[j]=='R':
                c2 += 5
            elif i%2==0 and j%2!=0 and l[j]=='G':
                c2 += 3
            elif i%2!=0 and j%2==0 and l[j]=='G':
                c2 += 3
            elif i%2!=0 and j%2!=0 and l[j]=='R':
                c2 += 5
    print(min(c1,c2))
