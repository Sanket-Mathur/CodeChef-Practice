for _ in range(int(input())):
    N, Q = map(int, input().split())
    D = list(map(int, input().split()))
    X = list(map(int, input().split()))
    
    d = 1 
    for i in D:
        d *= i 
        
    for x in X:
        print(x // d, end=' ')
    print('')
