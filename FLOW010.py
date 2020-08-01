try:
    for _ in range(int(input())):
        C = input()
        if C == 'B' or C == 'b':
            print('BattleShip')
        elif C == 'C' or C == 'c':
            print('Cruiser')
        elif C == 'D' or C == 'd':
            print('Destroyer')
        else:
            print('Frigate')
except:
    pass
