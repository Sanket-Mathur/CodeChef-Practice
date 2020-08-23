try:
    def check(n):
        if n <= 5:
            return n
        return n + check(n // 2)
    for _ in range(int(input())):
        N = int(input())
        for i in range(N):
            input()
        print(check(N))
except:
    pass
