for t in range(int(input())):

    N = int(input())
    C = list(map(int, input().split()))

    count = 1
    fast = C[0]

    for c in range(1,len(C)):
        if C[c] <= fast:
            count += 1
            fast = C[c]
    
    print(count)