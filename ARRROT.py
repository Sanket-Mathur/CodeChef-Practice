from sys import stdin, stdout

n = int(stdin.readline())
s = sum(map(int, stdin.readline().split()))
q = int(stdin.readline())
l = map(int, stdin.readline().split())

for i in l:
    s *= 2
    stdout.write(f'{s % 1000000007}\n')
