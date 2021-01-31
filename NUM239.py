for _ in range(int(input())):
    L, R = map(int, input().split())
    count = 0
    for i in range(L, R+1):
        if str(i)[-1] in ['2','3','9']:
            count += 1 
    print(count)
