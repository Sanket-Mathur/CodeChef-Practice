for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    even = odd = 0
    for i in L:
        if i%2:
            odd += 1 
        else:
            even += 1 
    print(2 if N>1 and odd%2 else 1)
