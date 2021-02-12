for _ in range(int(input())):
    S = input().strip()
    days = 0
    curr, maxJ = 0, 0
    for i in S:
        if i == '#':
            if curr > maxJ:
                maxJ = curr
                days += 1
            curr = 0
        else:
            curr += 1
    print(days)
