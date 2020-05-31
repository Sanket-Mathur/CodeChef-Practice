T = int(input())
for t in range(T):
	N = int(input())
	L = list(map(int, input().split()))
	d, flag = 6, 1
	for i in L:
		if(i==0):
			d += 1
		elif(d<6):
			flag = 0
		else:
			d = 1
	if(flag):
		print('YES')
	else:
		print('NO')
