for _ in range(int(input())):
    N, K = map(int, input().split())
    L = sorted(map(int, input().split()))
    a, b = 0, N-1
    while a < b:
        if L[a] + L[b] < K:
            a += 1
        elif L[a] + L[b] > K:
            b -= 1 
        else:
            print('Yes')
            break
    else:
        print('No')
