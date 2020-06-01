for t in range(int(input())):

    for p in range(int(input())):

        a, b, c = map(int, input().split())

        if(b % 2 == 0 or a == c):
            print(int(b/2))
        else:
            print(int(b/2)+1)