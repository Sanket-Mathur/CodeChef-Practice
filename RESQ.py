from math import sqrt
for _ in range(int(input())):
    N = int(input())
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            print((N - i*i) // i)
            break
