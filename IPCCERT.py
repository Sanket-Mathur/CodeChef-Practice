N, M, K = map(int, input().split())
c = 0
for _ in range(N):
    L = list(map(int, input().split()))
    Q = L[-1]
    L.pop()
    if Q <= 10 and sum(L) >= M:
        c += 1 
print(c)
