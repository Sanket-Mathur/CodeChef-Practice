for t in range(int(input())):

    J = set(input())
    S = list(input())
    gems = 0

    for i in J:
        gems += S.count(i)
    print(gems)