input()
L = [0] + list(map(int, input().split()))
visited = set()
paths = []
cnt = 0
for i in range(1,len(L)):
    if i in visited:
        continue
    current = []
    curr = i
    while curr not in visited:
        current.append(curr)
        curr = L[curr]
        if curr == i:
            cnt += 1
            visited = visited.union(set(current))
            paths.append(current + [current[0]])
            break
print(cnt)
for i in paths:
    print(*i)
