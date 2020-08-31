for _ in range(int(input())):
    N = int(input())
    S1 = input()
    S2 = input()
    score = 0
    i = 0
    while i < N:
        if S2[i] == 'N':
            i += 1 
        elif S1[i] == S2[i]:
            score += 1 
            i += 1 
        else:
            i += 2 
    print(score)
