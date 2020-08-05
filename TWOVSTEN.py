try:
    for _ in range(int(input())):
        N = int(input())
        if N % 5 != 0:
            print(-1)
        elif N % 10 == 0:
            print(0)
        else:
            print(1)
except:
    pass
