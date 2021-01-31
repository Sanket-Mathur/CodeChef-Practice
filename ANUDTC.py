for _ in range(int(input())):
    N = int(input())
    if N > 360:
        print('n n n')
    else:
        res = []
        res.append('y' if 360%N == 0 else 'n')
        res.append('y')
        res.append('y' if N*(N+1)//2 <= 360 else 'n' )
        print(*res)
