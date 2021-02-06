for _ in range(int(input())):
    N = int(input())
    W = list(map(int, input().split()))
    L = list(map(int, input().split()))
    curr = W.index(1)
    count = 0
    for i in range(2,N+1):
        ind = W.index(i)
        if ind > curr:
            curr = ind
            continue
        jump = L[ind]
        while ind <= curr:
            ind += jump
            count += 1
        curr = ind 
    print(count)
