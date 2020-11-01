for _ in range(int(input())):
    N = int(input())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    S = 0
    for i,j in zip(A,B):
        S += min(i,j)
    print(S)
