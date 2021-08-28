from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    
    flag = True
    for i in range(N-1):
        if L[i] != L[i+1] - 1:
            flag = False
            break
    
    stdout.write(f'{N if flag else 1}\n')