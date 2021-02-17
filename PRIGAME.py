from sys import stdin, stdout

lookup = [0,0]
n = 1000005
mark = [True for i in range(n + 1)]
p = 2
while (p * p <= n):
    if (mark[p] == True): 
        for i in range(p * p, n + 1, p): 
            mark[i] = False
    p += 1
cnt = 0
for i in range(2, n-1):
    if mark[i]:
        cnt += 1
    lookup.append(cnt)
    
for _ in range(int(input())):
    X, Y = map(int, stdin.readline().strip().split())
    print('Divyam' if lookup[X] > Y else 'Chef')
