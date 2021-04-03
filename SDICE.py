from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    if N % 4 == 0:
        top = 4
        rest = N // 4 - 1 
    else:
        rest = N // 4
        top = N % 4
        
    value = rest * 44
    if rest:
        value += (60 if top==4 else (55 if top==3 else (44 if top==2 else 32)))
    else:
        value += (60 if top==4 else (51 if top==3 else (36 if top==2 else 20)))
    stdout.write('{}\n'.format(value))
    
