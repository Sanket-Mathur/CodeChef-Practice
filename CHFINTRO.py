try:
    N, R = map(int, input().split())
    for i in range(N):
        r = int(input())
        if r >= R:
            print('Good boi')
        else:
            print('Bad boi')
except:
    pass
