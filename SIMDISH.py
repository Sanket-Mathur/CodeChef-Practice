try:
    for _ in range(int(input())):
        A = input().split(' ')
        B = input().split(' ')
        c = 0
        for i in A:
            if i in B:
                c += 1
        print('similar' if c >= 2 else 'dissimilar')
except:
    pass
