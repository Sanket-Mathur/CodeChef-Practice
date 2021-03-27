from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    X, R, M = map(int, stdin.readline().split())
    R *= 60
    M *= 60
    if M < R:
        stdout.write('NO\n')
    elif X >= R:
        stdout.write('YES\n')
    else:
        M -= X
        possible = X
        possible += M // 2
        stdout.write('YES\n' if possible >= R else 'NO\n')
