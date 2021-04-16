from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    r, c = map(int, stdin.readline().split())
    m1 = [[''] * c for row in range(r)]
    m2 = [[''] * r for col in range(c)]
    for row in range(r):
        s = stdin.readline()
        for col in range(c):
            m1[row][col] = m2[col][row] = s[col]
    
    spoon = False
    for row in range(r):
        if spoon:
            break
        if 'spoon' in ''.join(m1[row]).lower():
            spoon = True
    for col in range(c):
        if spoon:
            break
        if 'spoon' in ''.join(m2[col]).lower():
            spoon = True
    
    stdout.write('{}\n'.format('There is a spoon!' if spoon else 'There is indeed no spoon!'))
