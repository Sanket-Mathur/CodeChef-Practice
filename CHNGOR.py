for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    ans = 0
    for i in L:
        ans |= i 
    print(ans)
