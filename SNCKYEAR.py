try:
    for _ in range(int(input())):
        year = int(input())
        if year in [2010, 2015, 2016, 2017, 2019]:
            print('HOSTED')
        else:
            print('NOT HOSTED')
except:
    pass
