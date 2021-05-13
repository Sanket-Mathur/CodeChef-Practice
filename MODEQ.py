from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    
    cnt = 0
    mod = [1] * (N+1)
    for a in range(2, N+1):
        i = M % a 
        cnt += mod[i]
        for b in range(i, N+1, a):
            mod[b] += 1
                
    stdout.write(f'{cnt}\n')
