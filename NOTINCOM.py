try:
    for _ in range(int(input())):
        N, M = map(int, input().split())
        A = set(map(int, input().split()))
        B = set(map(int, input().split()))
        c = 0
        for i in A:
            if i in B:
                c += 1 
        print(c)
except:
    pass
