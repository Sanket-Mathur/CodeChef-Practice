from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = sorted(map(int, stdin.readline().split()))
    cnt = 0
    i = 1
    for x in L:
        if x > i:
            stdout.write('Second\n')
            break
        cnt += i - x 
        i += 1
    else:
        stdout.write('First\n' if cnt % 2 else 'Second\n')
