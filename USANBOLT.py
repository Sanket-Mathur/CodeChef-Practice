from math import sqrt

for _ in range(int(input())):
    finish, distancetoBolt, tigerAccelaration, boltSpeed = map(int, input().split())
    tiger = sqrt(2 * (finish + distancetoBolt) / tigerAccelaration)
    bolt = finish / boltSpeed
    print('Bolt' if bolt < tiger else 'Tiger')
