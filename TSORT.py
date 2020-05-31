N = int(input())
l = []
for n in range(N):
    x = int(input())
    l.append(x)
l.sort()
print(*l, sep='\n')