from math import ceil, floor
try:
    def time(N, B, M):
        if N <= 1:
            return N*M 
        return ceil(N/2)*M + B + time(floor(N/2), B, M*2)
    
    for _ in range(int(input())):
        N, B, M = map(int, input().split())
        print(time(N, B, M))
except:
    pass
