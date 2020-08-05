try:
    for _ in range(int(input())):
        N = int(input())
        n = 0
        while(n * (n+1) / 2 <= N):
            n += 1
        print(n-1)
except:
    pass
