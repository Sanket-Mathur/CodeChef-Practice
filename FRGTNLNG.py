try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        words = input().split()
        phrases = []
        for k in range(K):
            phrases.extend(input().split())
        used = []
        for w in words:
            if w in phrases:
                used.append('YES')
            else:
                used.append('NO')
        print(*used)
except:
    pass
