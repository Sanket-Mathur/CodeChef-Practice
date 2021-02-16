for _ in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    s = sum(L)
    cnt = 0
    for i in L:
        if i + K > s - i:
            cnt += 1 
    print(cnt)
