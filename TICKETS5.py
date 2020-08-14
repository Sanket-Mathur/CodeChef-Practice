try:
    for _ in range(int(input())):
        S = input()
        if len(set(S)) != 2:
            print('NO')
        else:
            for i in range(len(S)-1):
                if S[i] == S[i+1]:
                    print('NO')
                    break
            else:
                print('YES')
except:
    pass
