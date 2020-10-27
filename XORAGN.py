for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    xor = 0
    for i in A:
        xor ^= i
    print(2 * xor)
