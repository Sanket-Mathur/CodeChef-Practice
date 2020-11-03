for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    
    c = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] == A[i] & A[j]:
                c += 1 
    print(c)
