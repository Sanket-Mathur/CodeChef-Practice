try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        data = 0
        for n in range(N):
            T, D = map(int, input().split())
            if T < K:
                K -= T 
                T = 0
            else:
                T -= K 
                K = 0
            data += T*D
        print(data - K)
except:
    pass
