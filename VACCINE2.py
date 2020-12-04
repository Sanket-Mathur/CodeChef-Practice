from math import ceil

for _ in range(int(input())):
    N, D = map(int, input().split())
    L = list(map(int, input().split()))
    risk = len(list(filter(lambda a: a <= 9 or a >= 80, L)))
    print(ceil(risk / D) + ceil((N-risk) / D))
