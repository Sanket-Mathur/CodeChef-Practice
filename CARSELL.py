T = int(input())
for test in range(T):
	N = int(input())
	P = list(map(int, input().split()))
	total = 0
	P.sort(reverse = True)
	for i in range(len(P)):
		m = P[i] - i
		if(m<0):
			m = 0
		total += m%1000000007
	print(total%1000000007)
