for _ in range(int(input())):
    N = int(input())
    S = {}
    for i in range(N):
        d, p = map(int, input().split())
        S[d] = p 
    Q = int(input())
    for q in range(Q):
        d, p = map(int, input().split())
        solved = 0
        for i in S.keys():
            if i <= d:
                solved += S[i]
            else:
                break
        print('Go Camp' if solved >= p else 'Go Sleep')
