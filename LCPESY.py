for _ in range(int(input())):
    A = sorted(input())
    B = sorted(input())
    a = b = 0
    cnt = 0
    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            cnt += 1 
            a += 1 
            b += 1 
        elif A[a] < B[b]:
            a += 1 
        else:
            b += 1
    print(cnt)
