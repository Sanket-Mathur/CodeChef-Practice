try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        if L.count(1) == 0:
            print('Beginner')
        elif L.count(1) == 1:
            print('Junior Developer')
        elif L.count(1) == 2:
            print('Middle Developer')
        elif L.count(1) == 3:
            print('Senior Developer')
        elif L.count(1) == 4:
            print('Hacker')
        else:
            print('Jeff Dean')
except:
    pass
