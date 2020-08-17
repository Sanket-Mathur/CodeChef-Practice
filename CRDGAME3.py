try:
    for _ in range(int(input())):
        Pc, Pr = map(int, input().split())
        Dc = Pc // 9; Dr = Pr // 9
        if Pc % 9: Dc += 1 
        if Pr % 9: Dr += 1 
        
        if Dc < Dr:
            print (0, Dc)
        else:
            print (1, Dr)
except:
    pass
