try:
    for _ in range(int(input())):
        S = int(input())
        if S < 1500:
            S = S * 2
        else:
            S = S + (S*0.98) + 500 
        print(S)
except:
    pass
