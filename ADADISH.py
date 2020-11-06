for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    
    if N == 1:
        print(sum(L))
    else:
        A = L[:-1]
        B = L[-1:]
        while(sum(A) - sum(B) > A[0]):
            B.append(A[0])
            del A[0]
        print(max(sum(A), sum(B)))
