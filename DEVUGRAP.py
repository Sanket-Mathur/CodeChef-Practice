try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        res = 0
        for i in A:
            if i < K:
                res += K-i
                continue
            x = i % K 
            res += min(x, K-x)
        print(res)
except:
    pass
