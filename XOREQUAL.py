from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline().strip())
    stdout.write(f'{pow(2, n-1, 1000000007)}\n')
