for _ in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    for i in range(N):
        if L[i] < K:
            print('NO', i+1)
            break
        elif L[i] > K and i < N-1:
            L[i+1] += L[i] - K 
    else:
        print('YES')
