for _ in range(int(input())):
    L = list(map(int, input().split()))
    S = input()
    cost = 0
    for i in range(97,123):
        if chr(i) not in S:
            cost += L[i-97]
    print(cost)
