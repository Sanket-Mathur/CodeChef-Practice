for _ in range(int(input())):
    N, X = map(int, input().split())
    L = list(input())
    visited = [X]
    for i in L:
        if i == 'R':
            X += 1 
        else:
            X -= 1 
        if X not in visited:
            visited.append(X)
    print(len(visited))
