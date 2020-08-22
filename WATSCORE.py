try:
    for _ in range(int(input())):
        N = int(input())
        d = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
        for n in range(N):
            p, s = map(int, input().split())
            if d[p] < s:
                d[p] = s 
        c = 0
        for i in d.keys():
            if i <= 8:
                c += d[i]
        print(c)
except:
    pass
