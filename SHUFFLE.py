from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, K = map(int, stdin.readline().split())
    L = list(map(int, stdin.readline().split()))
    partitions = []
    for i in range(K):
        partitions.append([])
    for i in range(N):
        partitions[i%K].append(L[i])
    for i in range(K):
        partitions[i].sort()
    final = []
    for i in range(N):
        final.append(partitions[i%K].pop(0))
    stdout.write('yes\n' if final == sorted(L) else 'no\n')
