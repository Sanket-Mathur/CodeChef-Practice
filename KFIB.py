N, K = map(int, input().split())

if N <= K:
    print(1)
else:
    ser = [1] * (N)
    for i in range(K,N):
        ser[i] = sum(ser[i-K:i]) % 1000000007
    print(ser[-1])
