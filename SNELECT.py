for _ in range(int(input())):
    S = list(input())
    for i in range(len(S)):
        if S[i] == 'm':
            if i > 0 and S[i-1] == 's':
                S[i-1] = '*'
            elif i < len(S)-1 and S[i+1] == 's':
                S[i+1] = '*'
    if S.count('m') == S.count('s'):
        print('tie')
    elif S.count('m') > S.count('s'):
        print('mongooses')
    else:
        print('snakes')
