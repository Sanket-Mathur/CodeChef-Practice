for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    if L[0] != 0:
        print(0)
    else:
        cnt = 0
        for i in L:
            if i <= cnt:
                cnt += 1 
            else:
                break
        print(cnt)
