from sys import stdin, stdout, maxsize

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    maxDist = 1
    ind = 0
    s = [(0, L[0]), (1, L[1])]
    for i in range(2, N):
        while len(s) > 1:
            if (s[-1][1] - s[-2][1]) / (s[-1][0] - s[-2][0]) <= (L[i] - s[-1][1]) / (i - s[-1][0]):
                del s[-1]
            else:
                break
        s.append((i, L[i]))
        maxDist = max(maxDist, (s[-1][0] - s[-2][0]))
    stdout.write('{}\n'.format(maxDist))
