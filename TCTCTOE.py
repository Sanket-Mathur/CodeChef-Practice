from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    grid = []
    winX = winO = 0
    o = x = 0
    for i in range(3):
        g = stdin.readline()
        grid.append(g)
        o += g.count('O')
        x += g.count('X')
    
    if x not in [o, o+1]:
        stdout.write('3\n')
        continue
    
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] == 'X':
                winX += 1 
            elif grid[i][0] == 'O':
                winO += 1
    
    for j in range(3):
        if grid[0][j] == grid[1][j] == grid[2][j]:
            if grid[0][j] == 'X':
                winX += 1 
            elif grid[0][j] == 'O':
                winO += 1
    
    if grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]:
        if grid[1][1] == 'X':
            winX += 1 
        elif grid[1][1] == 'O':
            winO += 1
    
    if (winX == 1 and winO == 0 and x == o+1) or (winX == 0 and winO == 1 and x == o) or (winX == winO == 0 and x + o == 9) or (winX == 2 and x + o == 9):
        stdout.write('1\n')
    elif winX == winO == 0 and x + o < 9:
        stdout.write('2\n')
    else:
        stdout.write('3\n')
