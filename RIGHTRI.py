count = 0
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    D = []
    D.append((x1-x2)**2 + (y1-y2)**2)
    D.append((x2-x3)**2 + (y2-y3)**2)
    D.append((x1-x3)**2 + (y1-y3)**2)
    D.sort()
    if D[0] + D[1] == D[2]:
        count += 1
print(count)
