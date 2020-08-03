try:
    for _ in range(int(input())):
        R = int(input())
        D = []
        for i in range(3):
            x = list(map(int, input().split()))
            D.append(x)
        dist = [(D[0][0]-D[1][0])**2+(D[0][1]-D[1][1])**2,(D[1][0]-D[2][0])**2+(D[1][1]-D[2][1])**2,(D[0][0]-D[2][0])**2+D[0][1]-D[2][1])**2]
        c = 0
        for d in dist:
            if d <= R**2:
                c += 1
        if c >= 2:
            print('yes')
        else:
            print('no')
except:
    pass
