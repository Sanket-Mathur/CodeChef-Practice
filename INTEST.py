n, k = map(int, input().split())
d = 0
for i in range(n):
	t = int(input())
	if(t % k == 0):
		d += 1
print(d)