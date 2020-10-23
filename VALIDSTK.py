for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    c = 0
    for i in L:
        if i == 1:
            c += 1
        elif i == 0:
            c -= 1
        if c < 0:
            print('Invalid')
            break
    else:
        print('Valid')
