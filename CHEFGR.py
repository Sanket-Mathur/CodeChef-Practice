from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    L = list(map(int, stdin.readline().split()))
    largest = max(L)
    required = 0
    for i in L:
        required += largest-i
    if required > M or (required < M and (M-required)%N != 0):
        stdout.write('No\n')
    else:
        stdout.write('Yes\n')
