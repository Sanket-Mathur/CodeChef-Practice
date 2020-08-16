try:
    for _ in range(int(input())):
        N = int(input())
        seat = N % 8 if (N % 8) else 8 
        if not seat % 8:
            print(str(N-1) + 'SL')
        elif not seat % 7:
            print(str(N+1) + 'SU')
        elif not seat % 6:
            print(str(N-3) + 'UB')
        elif not seat % 5:
            print(str(N-3) + 'MB')
        elif not seat % 4:
            print(str(N-3) + 'LB')
        elif not seat % 3:
            print(str(N+3) + 'UB')
        elif not seat % 2:
            print(str(N+3) + 'MB')
        else:
            print(str(N+3) + 'LB')
except:
    pass
