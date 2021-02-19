while True:
    N = int(input())
    if N == 0:
        break
    L = sorted(map(int, input().split()))
    if N < 3:
        print(0)
    else:
        cnt = 0
        for i in range(N-1, 1, -1):
            p1 = 0
            p2 = i-1
            while p2 > p1:
                if L[i] > L[p1] + L[p2]:
                    cnt += p2-p1 
                    p1 += 1 
                else:
                    p2 -= 1 
        print(cnt)
