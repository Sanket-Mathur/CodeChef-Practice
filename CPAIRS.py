for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    c = res = 0
    for i in L:
        if i % 2 == 0:
            c += 1 
        else:
            res += c 
    print(res)
