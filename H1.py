prime = [2,3,5,7,11,13,17]
edges = [(0,3), (0,1), (1,2), (1,4), (2,5), (3,4), (3,6), (4,5), (4,7), (5,8), (6,7), (7,8)]

x = (1, 2, 3, 4, 5, 6, 7, 8, 9)

avail = {x: 0}
queue = [x]
while queue:
    current = queue.pop(0)
    for e in edges:
        if current[e[0]] + current[e[1]] in prime:
            nxt = list(current)
            nxt[e[0]], nxt[e[1]] = nxt[e[1]], nxt[e[0]]
            nxt = tuple(nxt)
            if nxt not in avail:
                avail[nxt] = avail[current] + 1 
                queue.append(nxt)

for _ in range(int(input())):
    input()
    grid = ()
    for i in range(3):
        grid += tuple(map(int, input().split()))
    print(avail[grid] if grid in avail else -1)
