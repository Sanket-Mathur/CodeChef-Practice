from sys import stdin, stdout

N, Q = map(int, stdin.readline().split())
rows = [0] * N 
cols = [0] * N 
maxR = maxC = 0
for q in range(Q):
    oper, ind, val = stdin.readline().split()
    ind = int(ind) - 1
    if oper == 'RowAdd':
        rows[ind] += int(val)
        if maxR < rows[ind]:
            maxR = rows[ind]
    else:
        cols[ind] += int(val)
        if maxC < cols[ind]:
            maxC = cols[ind]
stdout.write(str(maxR + maxC))
