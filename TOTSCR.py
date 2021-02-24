from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, K = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    for i in range(N):
        score = 0
        S = stdin.readline()
        for i in range(K):
            if S[i] == '1':
                score += A[i]
        stdout.write('{}\n'.format(score))
