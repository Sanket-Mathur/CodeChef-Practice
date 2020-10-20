for _ in range(int(input())):
    N, K, E, M = map(int, input().split())
    L = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l)
    marks = []
    for i in range(N-1):
        marks.append(sum(L[i]))
    sergey = sum(L[-1])
    marks.sort()
    if marks[N-K-1] - sergey + 1 > M:
        print("Impossible")
    elif marks[N-K-1] - sergey + 1 < 0:
        print(0)
    else:
        print(marks[N-K-1] - sergey + 1)
    
