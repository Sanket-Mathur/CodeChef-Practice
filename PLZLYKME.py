for _ in range(int(input())):
    L, D, S, C = map(int, input().split())
    count = S
    for i in range(D-1):
        count += count*C
        if count >= L:
            break
    print('ALIVE AND KICKING' if count >= L else 'DEAD AND ROTTING')
