from math import ceil
for _ in range(int(input())):
    N, K, Y = map(int, input().split())
    req = K*Y 
    days = Y - (Y // 7)
    if days*N < req:
        print(-1)
    else:
        print(ceil(req/N))
