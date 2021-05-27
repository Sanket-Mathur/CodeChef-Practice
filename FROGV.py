from sys import stdin, stdout

n, k, p = map(int, stdin.readline().split())
l = list(map(int, stdin.readline().split()))
s = sorted(l)

reach = {x:x for x in l}
reach[s[-1]] += k 
for i in range(n-2, -1, -1):
    if s[i+1] - s[i] <= k:
        reach[s[i]] = reach[s[i+1]]
    else:
        reach[s[i]] += k 

for i in range(p):
    pair = tuple(map(int, stdin.readline().split()))
    if reach[l[pair[0] - 1]] == reach[l[pair[1] - 1]]:
        stdout.write('Yes\n')
    else:
        stdout.write('No\n')
