from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    a = int(stdin.readline(), 2)
    b = int(stdin.readline(), 2)
    xor = list(bin(a ^ b)[2:])
    cnt = 0
    for i in range(len(xor)):
        if xor[i] == '1':
            cnt += 1
            for j in range(i, len(xor), 2):
                if xor[j] == '0':
                    break
                xor[j] = '0'
    stdout.write(f'{cnt}\n')
