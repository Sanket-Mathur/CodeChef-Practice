from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    grid = [stdin.readline() for i in range(N)]
    rect = ''
    flag = True
    ended = False
    for i in grid:
        if rect.count('1') == 0:
            rect = i 
        else:
            if i.count('1') == 0:
                ended = True
            elif i != rect or ended:
                flag = False
                break
    stdout.write('YES\n' if flag else 'NO\n')
