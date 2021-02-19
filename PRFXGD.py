for _ in range(int(input())):
    S = input()
    K, X = map(int, input().split())
    d = dict()
    for i in S:
        if i not in d:
            d[i] = 1 
        elif d[i] + 1 > X:
            if K == 0:
                break
            else:
                K -= 1 
        else:
            d[i] += 1
    print(sum(d.values()))
