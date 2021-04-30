from sys import stdin, stdout
from collections import Counter

for _ in range(int(stdin.readline())):
    n, w, wr = map(int, stdin.readline().split())
    l = Counter(map(int, stdin.readline().split()))
    if wr >= w:
        stdout.write('YES\n')
    else:
        w -= wr 
        weight = 0
        for (k,v) in l.items():
            if v > 1:
                weight += 2 * k * (v // 2)
            if weight >= w:
                stdout.write('YES\n')
                break
        else:
            stdout.write('NO\n')
