from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    if N > 62:
        stdout.write('NO\n')
    else:
        s = set()
        for i in range(N):
            oper = 0
            for j in range(i,N):
                oper |= L[j]
                s.add(oper)
        stdout.write('YES\n' if len(s) == N*(N+1)//2 else 'NO\n')
