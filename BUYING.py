for _ in range(int(input())):
    N, X = map(int, input().split())
    L = sorted(map(int, input().split()))
    rem = sum(L) % X 
    if L[0] <= rem:
        print(-1)
        continue
    else:
        print(sum(L) // X)
