for _ in range(int(input())):
    P1, P2, K = map(int, input().split())
    P = (P1 + P2) // K
    print('COOK' if P % 2 else 'CHEF')
