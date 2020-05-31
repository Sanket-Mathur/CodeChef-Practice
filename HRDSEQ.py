T = int(input())
for t in range(T):
	N = int(input())
	L = [0]
	while(len(L) < N):
		x = L[-1]
		k = -1
		for i in range(len(L)-2, -1, -1):
			if L[i] == x:
				k = i
				break
		if(k==-1):
			L.append(0)
		else:
			L.append(len(L)-1-k)
	print(L.count(L[-1]))
