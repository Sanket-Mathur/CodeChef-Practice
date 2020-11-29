for _ in range(int(input())):
    N = int(input())
    print('O', end='')
    for i in range(1,N):
        if i % 8 == 0:
            print('')
        print('.', end='')
    for i in range(N,64):
        if i % 8 == 0:
            print('')
        print('X', end='')
    print('')
