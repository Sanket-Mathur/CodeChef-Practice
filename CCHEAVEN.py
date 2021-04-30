from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '1':
            cnt += 1 
        if cnt / (i+1) >= 0.5:
            stdout.write('YES\n')
            break
    else:
        stdout.write('NO\n')
