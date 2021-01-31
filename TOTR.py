N, S = input().split()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
d = {}
for i in range(26):
    d[alphabets[i]] = S[i]

for _ in range(int(N)):
    S = input()
    for i in S:
        if i == '_':
            print(' ', end='')
        elif i.lower() in d:
            if i.islower():
                print(d[i], end='')
            else:
                print(d[i.lower()].upper(), end='')
        else:
            print(i, end='')
    print('')
