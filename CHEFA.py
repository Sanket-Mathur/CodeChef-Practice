for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()), reverse=True)
    print(sum(L[0:N:2]))
