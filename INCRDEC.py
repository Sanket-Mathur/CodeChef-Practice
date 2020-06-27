for T in range(int(input())):

    N = int(input())
    S = list(map(int, input().split()))
    flag = 0

    for s in S:
        if S.count(s) >= 3:
            flag += 1
    
    if S.count(max(S)) > 1:
        flag += 1
    
    if flag != 0:
        print('NO')
        continue

    print('YES')
    S.sort()
    for i in range(N-1):
        if S[i] != S[i+1]:
            print(S[i], end = ' ')
    print(max(S), end = ' ')
    for i in range(N-1, 0, -1):
        if S[i] == S[i-1]:
            print(S[i], end = ' ')
    print('')
