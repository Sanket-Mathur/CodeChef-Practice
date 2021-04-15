from sys import stdin, stdout

MOD = 10**9 + 7

for _ in range(int(stdin.readline())):
    n, a = map(int, stdin.readline().split())
    res = 0
    for i in range(1,n+1):
        x = pow(a, 2 * i - 1, MOD)
        res = (res + x) % MOD
        a = (a * x) % MOD
    stdout.write(f'{res}\n')
