try:
    N = int(input())
    if N % 4 == 0:
        N += 1
    else:
        N -= 1
    print(N)
except:
    pass
