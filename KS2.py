for _ in range(int(input())):
    N = input()
    digits = list(map(int, list(N)))
    print(N + str((10 - sum(digits) % 10) % 10))
