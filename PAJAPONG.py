for _ in range(int(input())):
    X, Y, K = map(int, input().split())
    turn = (X+Y) // K
    print('Paja' if turn%2 else 'Chef')
