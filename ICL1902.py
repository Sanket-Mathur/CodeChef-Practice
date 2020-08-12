from math import sqrt
try:
    for _ in range(int(input())):
        N = int(input())
        c = 0
        while N >= 1:
            x = int(sqrt(N))
            N -= x**2
            c += 1
        print(c)
except:
    pass
