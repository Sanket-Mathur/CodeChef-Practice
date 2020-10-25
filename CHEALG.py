for _ in range(int(input())):
    S = input()
    res = ''
    
    c = 1
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            c += 1 
        else:
            res += S[i] + str(c)
            c = 1
    res += S[-1] + str(c)
    
    print('YES' if len(res) < len(S) else 'NO')
