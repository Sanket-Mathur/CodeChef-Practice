from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    for i in range(n):
        if (i+1) % l[i] or l[i] > (i+1):
            stdout.write('NO\n')
            break
    else:
        stdout.write('YES\n')
