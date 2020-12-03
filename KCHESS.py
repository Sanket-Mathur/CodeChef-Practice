for _ in range(int(input())):
    N = int(input())
    kX, kY = [], []
    for i in range(N):
        t1, t2 = map(int, input().split())
        kX.append(t1)
        kY.append(t2)
    A, B = map(int, input().split())
    if A in kX or B in kY:
        print('YES')
    else:
        print('NO')
