N = int(input())
m, c = map(int, input().split())

V1, V2 = [0], [0]

for i in range(N):
    X, Y, P = map(int, input().split())
    y = m*X + c 
    if Y > y:
        V1.append(P)
    else:
        V2.append(P)

print(max(sum(V1), sum(V2)))
