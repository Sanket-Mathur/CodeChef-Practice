try:
    for _ in range(int(input())):
        L = list(map(int, input().split()))
        R = []
        for l in L:
            if l % 2 == 0:
                R.append(1)
            else:
                R.append(0)
        if R.count(1) > R.count(0):
            print('READY FOR BATTLE')
        else:
            print('NOT READY')
except:
    pass
