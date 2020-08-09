import math
try:
    for _ in range(int(input())):
        A, B, N = map(int, input().split())
        if N%2 == 1:
            A *= 2
        print(max(A,B) // min(A,B))
except:
    pass
