from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
nl = []
ml = []

for _ in range(n):
    nl.append(tuple(map(int, stdin.readline().split())))
for _ in range(m):
    ml.append(tuple(map(int, stdin.readline().split())))

nl.sort(key = lambda x: x[0])
ml.sort(key = lambda x: x[0])

i = j = 0
cnt = 0
while (i < n and j < m):
    a = nl[i]
    b = ml[j]
    
    if a[1] < b[0]:
        i += 1 
    elif b[1] < a[0]:
        j += 1
    else:
        cnt += max(a[1], b[1]) - min(a[0], b[0]) - abs(a[0] - b[0]) - abs(a[1] - b[1])
        if a[1] < b[1]:
            i += 1
        else:
            j += 1

stdout.write(f'{cnt}\n')