for T in range(int(input())):
    M, N = map(int, input().split())
    R = list(map(int, input().split()))
    L = int(input())
    S = input()
    loc = [0,0]
    for i in S:
        if i == 'U':
            loc[1] += 1 
        elif i == 'D':
            loc[1] -= 1 
        elif i == 'R':
            loc[0] += 1 
        else:
            loc[0] -= 1 
    if loc[0] < 0 or loc[0] > M or loc[1] < 0 or loc[1] > N:
        print('Case {}: {}'.format(T+1, 'DANGER'))
    elif loc == R:
        print('Case {}: {}'.format(T+1, 'REACHED'))
    else:
        print('Case {}: {}'.format(T+1, 'SOMEWHERE'))

