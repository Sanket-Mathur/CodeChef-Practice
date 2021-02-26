from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, K = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    s = {K}
    for i in A:
        dup = s.copy()
        for j in dup:
            s.add(i^j)
    stdout.write('{}\n'.format(max(s)))
