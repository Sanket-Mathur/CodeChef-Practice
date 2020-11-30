days = {'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':7}

for _ in range(int(input())):
    S, E, L, R = input().split()
    L = int(L)
    R = int(R)
    min_days = (days[E] - days[S] + 8) % 7
    c = R+1 
    for i in range(L, R+1):
        if i % 7 == min_days:
            c = i 
            break
    if c > R:
        print('impossible')
    elif c+7 <= R:
        print('many')
    else:
        print(c)
