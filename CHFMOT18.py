for _ in range(int(input())):
    S, N = map(int, input().split())
    c = S // N 
    S %= N 
    if S > 0:
        c += (2 if (S%2 and S>1) else 1)
    print(c)
