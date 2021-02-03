for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()), reverse=True)
    i = paid = total = 0
    while i < len(L):
        if paid < 2:
            total += L[i]
            i += 1 
            paid += 1 
        else:
            i += 2
            paid = 0
    print(total)
