try:
    for _ in range(int(input())):
        N = int(input())
        c = 0
        for n in range(N):
            x, y = map(int, input().split())
            if y-x > 5: c += 1
        print(c)
except:
    pass
