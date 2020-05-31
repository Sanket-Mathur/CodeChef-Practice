T = int(input())
for t in range(T):
	L, K = map(int, input().split())
	F = list()
	for k in range(K,-1,-1):
		F.append(L-k)
	for r in range(1,L):
		if r not in F:
			F.append(r)
	print(*F)