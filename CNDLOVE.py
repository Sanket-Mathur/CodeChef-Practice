try:
    for _ in range(int(input())):
        N = int(input())
        L = sum(list(map(int, input().split())))
        print('YES' if L % 2 else 'NO')
except:
    pass
