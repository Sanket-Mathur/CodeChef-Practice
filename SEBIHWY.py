for _ in range(int(input())):
    S, SG, FG, D, T = map(int, input().split())
    speed = (D*180)/T + S
    if abs(SG-speed) == abs(FG-speed):
        print('DRAW')
    elif abs(SG-speed) > abs(FG-speed):
        print('FATHER')
    else:
        print('SEBI')
