for _ in range(int(input())):
    S = input()
    count = 0
    for i in S:
        if i.isdigit():
            count += int(i)
    print(count)
