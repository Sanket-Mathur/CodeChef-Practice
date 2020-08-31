for _ in range(int(input())):
    N = int(input())
    D = {}
    for n in range(N):
        x = input()
        if x in D:
            D[x] += 1 
        else:
            D[x] = 1
    teams = list(D.keys())
    scores = list(D.values())
    if len(teams) == 1:
        print(teams[0])
    elif len(teams) == 2:
        if scores[0] == scores[1]:
            print('Draw')
        elif scores[0] > scores[1]:
            print(teams[0])
        else:
            print(teams[1])
    else:
        print('Draw')
