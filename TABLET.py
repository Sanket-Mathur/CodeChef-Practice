try:
    for _ in range(int(input())):
        N, B = map(int, input().split())
        area = 0
        for n in range(N):
            W, H, P = map(int, input().split())
            if P <= B and area < W*H:
                area = W*H 
        print(area if area != 0 else 'no tablet')
except:
    pass
