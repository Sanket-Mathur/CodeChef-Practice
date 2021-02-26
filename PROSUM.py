from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    c1 = c2 = 0
    for i in L:
        if i > 2:
            c1 += 1 
        elif i  == 2:
            c2 += 1
    print((c1**2 + 2*c1*c2 - c1) // 2)
