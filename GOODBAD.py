try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        S = input()
        u = l = 0
        for i in S:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1
        if min(l,u) > K:
            print('none')
        elif max(l,u) <= K or l == u:
            print('both')
        elif u > l:
            print('brother')
        else:
            print('chef')
except:
    pass
