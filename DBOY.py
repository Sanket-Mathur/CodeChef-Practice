from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    H = sorted(map(int, stdin.readline().split()))
    F = sorted(map(int, stdin.readline().split()))
    cnt = 0
    lookup = [0] + [10**9]*(H[-1]*2)
    for i in range(1, H[-1]*2 + 1):
        for j in F:
            temp = i - j
            if temp < 0:
                break
            lookup[i] = min(lookup[i], lookup[temp]+1)
    for i in H:
        cnt += lookup[2*i]
    stdout.write('{}\n'.format(cnt))
