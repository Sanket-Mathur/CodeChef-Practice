for _ in range(int(input())):
    
    N, K, X, Y = map(int, input().split())

    if X == Y:
        print('YES')
        exit(0)
    C = (X + K) % N 
    while C != X:
        if C == Y:
            print('YES')
            break
        C = (C + K) % N 
    else:
        print('NO')
