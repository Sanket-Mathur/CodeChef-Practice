from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    stdin.readline()
    stdout.write('1\n' if sum(list(map(int, stdin.readline().split()))) % 2 == 0 else '2\n')
    
