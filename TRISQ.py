try:
    def sol(n):
        n //= 2
        return (n * (n-1)) // 2
    for _ in range(int(input())):
        N = int(input())
        print(sol(N))
except:
    pass
