for _ in range(int(input())):
    S = input().strip()
    N = int(S)
    count = 0
    for i in S:
        if i != '0' and N % int(i) == 0:
            count += 1 
    print(count)
