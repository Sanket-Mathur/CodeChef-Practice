try:
    for _ in range(int(input())):
        S1 = input()
        S2 = input()
        mind = maxd = 0
        for i in range(len(S1)):
            if S1[i] == '?' or S2[i] == '?':
                maxd += 1 
            elif S1[i] != S2[i]:
                mind += 1
                maxd += 1
        print(mind, maxd)
except:
    pass
