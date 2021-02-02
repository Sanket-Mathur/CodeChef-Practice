for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    c, p = 0, L[0]
    count = 0
    for i in L:
        if p < i:
            p = i
            c += 1 
        count += c 
    print(count)
