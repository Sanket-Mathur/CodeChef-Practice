T = int(input())
for t in range(T):
	N, Q = map(int, input().split())
	m = l = 0
	for q in range(Q):
		f, d = map(int, input().split())
		m += abs(l-f)
		m += abs(d-f)
		l = d
	print(m)