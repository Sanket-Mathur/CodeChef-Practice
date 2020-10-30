for _ in range(int(input())):
    a, b, n = map(int, input().split())
    if a == b or ( n % 2 == 0 and abs(a) == abs(b)):
        print(0)
    elif n % 2 == 0:
        print(1 if abs(a) > abs(b) else 2)
    else:
        print(1 if a > b else 2)
