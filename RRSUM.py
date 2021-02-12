N, M = map(int, input().split())
l, r = N+2, 3*N
for i in range(M):
    q = int(input())
    if q < l or q > r:
        print(0)
    else:
        print(min(q-l+1, r-q+1))
