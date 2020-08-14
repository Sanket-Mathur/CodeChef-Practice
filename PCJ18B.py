try:
    for _ in range(int(input())):
        N = int(input())
        c = 0 if not N%2 else 1
        for i in range(N//2):
            c += (N - 2*i)**2
        print(c)
except:
    pass
