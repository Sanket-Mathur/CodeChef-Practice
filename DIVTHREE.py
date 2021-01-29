for _ in range(int(input())):
    N, K, D = map(int, input().split())
    T = sum(map(int, input().split()))
    print(min(T // K, D))
