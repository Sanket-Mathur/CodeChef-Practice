for _ in range(int(input())):
    N, B, M = map(int, input().split())
    Lm = list(map(int, input().split()))
    
    curr, c = -1, 0
    for i in Lm:
        load = i // B 
        if load != curr:
            curr = load 
            c += 1 
    
    print(c)
