N = int(input())
L = list(map(int, input().split()))
conn = [0]*N
for i in range(N):
    if L[i] != 0:
        conn[L[i]-1] += 1 
[print(i+1, end=' ') for i in range(N) if conn[i] == 0]
