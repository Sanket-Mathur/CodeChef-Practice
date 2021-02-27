from sys import stdin, stdout
from collections import Counter

for _ in range(int(stdin.readline())):
    S = stdin.readline().strip()
    cnt = Counter(S)
    pair = ones = 0
    for i in cnt.values():
        if i == 1:
            ones += 1
        elif i % 2 == 0:
            pair += i // 2
        else:
            pair += (i - 3) // 2
    if pair >= ones:
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')
