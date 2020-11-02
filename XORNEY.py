from sys import stdin, stdout 

for _ in range(int(input())):
    L, R = map(int, stdin.readline().split())
    
    count = ((R-L) // 2) + 1 if L % 2 or R % 2 else (R-L) // 2
    stdout.write('Odd\n' if count % 2 else 'Even\n')
