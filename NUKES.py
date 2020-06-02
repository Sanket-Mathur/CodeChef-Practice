A, N, K = map(int, input().split())

chambers = [0]*K

for i in range(K):
    if A != 0:
        chambers[i] = int(A % (N+1))
        A = int(A / (N+1))

print(*chambers)