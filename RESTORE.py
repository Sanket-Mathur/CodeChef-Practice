for _ in range(int(input())):
    N = int(input())
    B = list(map(int, input().split()))
    
    A = [0] * N
    curr = 2
    for i in range(N-1,-1,-1):
        if B[i] == i+1:
            A[i] = curr
            curr += 1
        else:
            A[i] = A[B[i]-1]
    
    print(*A)
