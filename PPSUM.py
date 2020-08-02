try:
    def sum(D, N):
        if D == 1:
            return (N * (N+1)/2)
        return sum(D-1, N * (N+1)/2)
    for _ in range(int(input())):
        a,b = map(int, input().split())
        print(int(sum(a,b)))
except:
    pass
