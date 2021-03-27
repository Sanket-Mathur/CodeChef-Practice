from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    A, Y, X = map(int, stdin.readline().split())
    if Y <= A:
        stdout.write('{}\n'.format(Y*X))
    else:
        stdout.write('{}\n'.format(1 + A*X))
