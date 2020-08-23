try:
    for _ in range(int(input())):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        scores = [A[i]*20 - B[i]*10 for i in range(N) if A[i]*20 - B[i]*10 >= 0]
        print(0 if not scores else max(scores))
except:
    pass
