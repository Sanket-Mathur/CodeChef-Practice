a, b, c = map(int, input().split())
A = []
for i in range(a+b+c):
    A.append(int(input()))
A.sort()

i = 0
B = []
while i < len(A)-1:
    if A[i] == A[i+1]:
        B.append(A[i])
        i += 1
    i += 1
print(len(B))
print(*B, sep='\n')
