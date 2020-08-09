try:
    for _ in range(int(input())):
        N = int(input())
        ans = 0
        for i in range(1, N+1):
            input()
            ans = ans ^ i
        print(ans)
except:
    pass
