N = int(input())
total = sum(list(map(int, input().split())))
required = N*(N+1)/2
print('YES' if required == total else 'NO')
