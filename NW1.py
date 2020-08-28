days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
for _ in range(int(input())):
    N, D = input().split()
    N = int(N)
    r = N % 7
    if not r:
        print(*[N // 7]*7)
    else:
        L = [N // 7]*7
        i = days.index(D)
        for x in range(i, i+r):
            if x < 7:
                L[x] += 1
            else:
                L[x-7] += 1
        print(*L)
