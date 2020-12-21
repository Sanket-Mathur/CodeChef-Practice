for _ in range(int(input())):
    x,y,K,N = map(int, input().split())
    if x==y:
        print('Yes')
    elif abs(y-x) >= K and (abs(y-x) // K) % 2:
        print('No')
    elif abs(y-x) % K:
        print('No')
    else:
        print('Yes')
