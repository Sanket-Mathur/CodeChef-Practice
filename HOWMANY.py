try:
    N = str(int(input())) # converting it to int before to avoid inputs starting with a 0
    if len(N) <= 3:
        print(len(N))
    else:
        print('More than 3 digits')
except:
    pass
