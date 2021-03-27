from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    res = [0]*N 
    start = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] < L[j]:
                break
            elif L[i] == L[j]:
                res[i] += 1 
                res[j] += 1 
        stdout.write('{} '.format(res[i]))
    stdout.write('\n')
