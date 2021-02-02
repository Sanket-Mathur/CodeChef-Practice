def match(a,b):
    p1 = p2 = 0
    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            p1 += 1 
            p2 += 1 
        else:
            p2 += 1
    if p1 == len(a):
        return True
    return False
for _ in range(int(input())):
    M, W = input().split()
    flag = match(M,W)
    if not flag:
        flag = match(W,M)
    print('YES' if flag else 'NO')
