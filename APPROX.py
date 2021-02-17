for _ in range(int(input())):
    N = int(input())
    if N == 0:
        print(3)
        continue
    S = ''
    n, d = 103993, 33102
    while len(S) <= N:
        S += str(n//d)
        n = n%d * 10 
    print('3.' + S[1:])
