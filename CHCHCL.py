try:
    for _ in range(int(input())):
        M, N = map(int, input().split())
        if M*N % 2:
            print('No')
        else:
            print('Yes')
except:
    pass
