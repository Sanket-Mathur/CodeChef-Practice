from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    directions = []
    streets = []
    for i in range(n):
        d, *s = stdin.readline().split()
        directions.append(d)
        streets.append(s)
    res = 'Begin ' + ' '.join(streets[-1])
    for i in range(n-2, -1, -1):
        stdout.write(f'{res}\n')
        res = ('Left ' if directions[i+1] == 'Right' else 'Right ') + ' '.join(streets[i])
    stdout.write(f'{res}\n\n')
