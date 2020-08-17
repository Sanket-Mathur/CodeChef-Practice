try:
    for _ in range(int(input())):
        H, P = map(int, input().split())
        h = H // 2
        h = h+2 if h % 2 == 0 else h+1
        print(1 if P>=h else 0)
except:
    pass
