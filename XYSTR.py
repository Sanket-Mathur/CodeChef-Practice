for _ in range(int(input())):
    S = input()
    i = c = 0
    while i < len(S)-1:
        if (S[i] == 'x' and S[i+1] == 'y') or (S[i] == 'y' and S[i+1] == 'x'):
            i += 2
            c += 1 
        else:
            i += 1 
    print(c)
