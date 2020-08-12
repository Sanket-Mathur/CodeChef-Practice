from math import sqrt
try:
    for _ in range(int(input())):
        N, V1, V2 = map(int, input().split())
        if (sqrt(2) / V1) < (2 / V2):
            print('Stairs')
        else:
            print('Elevator')
except:
    pass
