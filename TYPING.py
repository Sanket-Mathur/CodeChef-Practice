for _ in range(int(input())):
    d = {}
    time = 0
    left, right = ['d','f'], ['j','k']
    for n in range(int(input())):
        S = input()
        if S in d:
            time += d[S] // 2
        else:
            t = 2
            for i in range(1,len(S)):
                if (S[i] in left and S[i-1] in left) or (S[i] in right and S[i-1] in right):
                    t += 4
                else:
                    t += 2
            time += t 
            d[S] = t
    print(time)
