for _ in range(int(input())):
    A, B = map(int, input().split())
    if A%2==0 or B%2==0:
        print((A*B)//2)
    else:
        print((A*B)//2 + 1)
