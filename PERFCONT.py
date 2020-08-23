try:
    for _ in range(int(input())):
        N, P = map(int, input().split())
        L = list(map(int, input().split()))
        cakewalk = hard = 0
        for i in L:
            if i >= P//2:
                cakewalk += 1 
            elif i <= P//10:
                hard += 1
        if (cakewalk == 1) and (hard == 2):
            print('yes')
        else:
            print('no')
except:
    pass
