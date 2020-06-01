for t in range(int(input())):

    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    j = A[K-1]
    A.sort()
    print(A.index(j) + 1)