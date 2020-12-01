for _ in range(int(input())):
    N, H, Y1, Y2, L = map(int, input().split())
    count = 0
    for n in range(N):
        t, x = map(int, input().split())
        if L > 0 and ((t == 1 and H-Y1 <= x) or (t == 2 and Y2 >= x)):
            count += 1
            continue
        L -= 1 
        if L > 0:
            count += 1
    print(count)
