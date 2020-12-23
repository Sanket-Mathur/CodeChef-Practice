from itertools import combinations

for _ in range(int(input())):
    N, M = map(int, input().split())
    L = []
    for i in range(N):
        L.append(int(input()))
    L = list(filter(lambda x: x <= M, L))
    flag = False
    for i in range(1, N+1):
        for j in combinations(L, i):
            if sum(list(j)) == M:
                flag = True
                break
        if flag: break
    print('Yes' if flag else 'No')
