try:
    f = 0
    for _ in range(int(input())):
        S = input()
        if 'ch' in S or 'he' in S or 'ef' in S:
            f += 1
    print(f)
except:
    pass
