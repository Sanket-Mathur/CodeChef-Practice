from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n1, n2, m = map(int, stdin.readline().split())
    max_removal = m*(m+1) // 2 
    if max_removal >= min(n1, n2):
        stdout.write('{}\n'.format(abs(n1-n2)))
    else:
        stdout.write('{}\n'.format(n1 + n2 - 2*max_removal))
