try:
    for _ in range(int(input())):
        S1 = input()
        S2 = input()
        for i in range(len(S1)):
            if S1[i] != S2[i] and S1[i] != '?' and S2[i] != '?':
                print('No')
                break
        else:
            print('Yes')
except:
    pass
