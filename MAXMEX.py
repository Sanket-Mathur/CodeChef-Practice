from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    L = sorted(map(int, stdin.readline().split()))
    S = set(L)
    m = -1
    for i in range(1,N+1):
        if i not in S:
            m = i 
            break
    if M > m:
        stdout.write('-1\n')
    elif M == m:
        stdout.write('{}\n'.format(N))
    else:
        stdout.write('{}\n'.format(N - L.count(M)))
