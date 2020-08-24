try:
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if (a % 2 and b == a+1) or (not a % 2 and b == a-1) or (b == a+2 or b == a-2):
            print('YES')
        else:
            print('NO')
except:
    pass
