from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    s = sorted(L, reverse=True)
    d = {}
    cnt = 1
    for i in s:
        if i in d:
            d[i].append(cnt)
        else:
            d[i] = [cnt]
        cnt += 1 
    for i in L:
        stdout.write('{} '.format(d[i][0]))
        del d[i][0]
    stdout.write('\n')
