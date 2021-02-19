for _ in range(int(input())):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    maxElement, minElement = max(L), min(L)
    for i in range(N):
        print(max(abs(i-maxElement), abs(i-minElement)), end = ' ')
    print('')
