try:
    for _ in range(int(input())):
        N = int(input())
        A = list(map(int, input().split()))
        M = int(input())
        B = list(map(int, input().split()))
        a = b = 0
        while a < len(A) and b < len(B):
            if B[b] == A[a]:
                b += 1 
                a += 1 
            else:
                a += 1 
        if b == len(B):
            print('Yes')
        else:
            print('No')
except:
    pass
