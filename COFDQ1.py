N = int(input())
L = list(map(int, input().split()))
S = int(input())
i, j = 0, S
res = []
while j <= N:
    K = sorted(L[i:j])
    if S % 2 == 1:
        res.append(K[S//2])
    else:
        res.append((K[S//2-1] + K[S//2])/2)
    i += 1 
    j += 1
print(*res)
