days = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}

for _ in range(int(input())):
    S, E, L, R = input().split()
    L = int(L)
    R = int(R)
    
    min_days = (days[E] - days[S] + 8) % 7

    possible = False
    while min_days <= R:
        if min_days >= L:
            possible = True
            if min_days+7 <= R:
                print('many')
            else:
                print(min_days)
            break
        min_days += 7
    if not possible:
        print('impossible')
