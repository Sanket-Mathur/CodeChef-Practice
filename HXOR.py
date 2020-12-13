import math

for _ in range(int(input())):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    for x in range(X):
        if A[i] == 0:
            while i < N-2 and A[i] == 0:
                i += 1 
        if A[i] != 0:
            p = 2**int(math.log(A[i], 2))
        elif len(A) > 2 or (X-x) % 2 == 0:
            break
        else:
            A[i] = 1 
            A[i+1] ^= 1 
            break
        j = i+1 
        while j < N-1 and A[j]^p > A[j]:
            j += 1 
        A[i] ^= p 
        A[j] ^= p 
    print(*A)
