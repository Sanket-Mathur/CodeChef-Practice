from sys import stdin, stdout
from collections import Counter

for _ in range(int(stdin.readline())):
    p = Counter(stdin.readline().strip())
    n = int(stdin.readline())
    
    s = ''
    for i in range(n):
        s += stdin.readline().strip()
    
    for key,val in Counter(s).items():
        if p[key] < val:
            stdout.write('NO\n')
            break
    else:
        stdout.write('YES\n')

