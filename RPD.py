from itertools import combinations

try:
    for _ in range(int(input())):
        N = int(input())
        L = list(map(int, input().split()))
        max_sum = 0
        for i in combinations(L,2):
            p = i[0] * i[1]
            s = 0
            for d in list(str(p)):
                s += int(d)
            if s > max_sum:
                max_sum = s 
        print(max_sum)
except:
    pass
