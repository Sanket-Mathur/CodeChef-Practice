from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = bin(int(stdin.readline()))[2:]
    A = ['1'] * len(N)
    B = ['1' if x == '0' else '0' for x in N]
    maxZor = 0
    for i in range(1, len(B)):
        if B[i] == '0':
            A[i] = '0'
            B[i] = '1'
    stdout.write('{}\n'.format(int(''.join(A),2) * int(''.join(B),2)))
