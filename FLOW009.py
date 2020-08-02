try:
    for _ in range(int(input())):
        Q, P = map(int, input().split())
        T = Q*P
        print(T if Q <= 1000 else T - T*0.1)
except:
    pass
