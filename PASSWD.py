for _ in range(int(input())):
    S = input()
    if len(S) < 10:
        print('NO')
    else:
        c = C = d = s = False
        for i in range(1,len(S)-1):
            if 97 <= ord(S[i]) <= 122:
                c = True
            elif 65 <= ord(S[i]) <= 122:
                C = True 
            elif 48 <= ord(S[i]) <= 57:
                d = True
            elif S[i] in ['@', '#', '%', '&', '?']:
                s = True
            if c and C and d and s:
                break
        if c and C and d and s:
            print('YES')
        elif C and d and s and ((97 <= ord(S[0]) <= 122) or (97 <= ord(S[-1]) <= 122)):
            print('YES')
        else:
            print('NO')
