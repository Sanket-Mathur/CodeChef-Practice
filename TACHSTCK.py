N, K = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))
L.sort()
i = count = 0
while i < N-1:
    if L[i+1] - L[i] <= K:
        count += 1 
        i += 1
    i += 1
print(count)
