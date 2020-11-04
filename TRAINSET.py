for _ in range(int(input())):
    N = int(input())
    S = {}
    for i in range(N):
        w, s = input().split()
        s = int(s)
        if w not in S:
            S[w] = [1,0] if s == 0 else [0,1]
        else:
            if s == 0:
                S[w][0] += 1 
            else:
                S[w][1] += 1 
    c = 0
    for i in S.values():
        c += max(i)
    print(c)
